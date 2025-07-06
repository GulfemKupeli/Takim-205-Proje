from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, validator, Field, ValidationError
from typing import Literal, Optional
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import json
import numpy as np
from typing import List
from sqlalchemy.orm import Session

# Veritabanı modüllerini içe aktar
from database import HealthRecord, get_db, create_tables

app = FastAPI(title="Kalp Sağlığı Risk Tahmin Sistemi")

# Veritabanı tablolarını oluştur
create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Risk hesaplama fonksiyonu
def calculate_heart_disease_risk(data: dict) -> dict:
    """
    Basit bir risk hesaplama fonksiyonu.
    Gerçek bir uygulamada daha karmaşık bir model kullanılmalıdır.
    """
    risk_score = 0
    
    # Yaş faktörü
    age_factor = min(1.0, data['age'] / 100)
    
    # Cinsiyet faktörü (erkeklerde daha yüksek risk)
    gender_factor = 1.2 if data['gender'] == 'male' else 1.0
    
    # Vücut kitle indeksi (BMI)
    height_in_meters = data['height'] / 100  # cm'den m'ye çevir
    bmi = data['weight'] / (height_in_meters ** 2)
    bmi_factor = min(2.0, bmi / 25)  # 25 üzeri BMI için artan risk
    
    # Tansiyon faktörü
    bp_factor = 1.0
    if data['systolic_bp'] >= 140 or data['diastolic_bp'] >= 90:
        bp_factor = 1.5
    
    # Kolesterol oranı
    cholesterol_ratio = data['cholesterol_ldl'] / data['cholesterol_hdl']
    cholesterol_factor = min(2.0, cholesterol_ratio / 3)
    
    # Sigara faktörü
    smoker_factor = 1.5 if data['smoker'] else 1.0
    
    # Alkol faktörü
    alcohol_factor = 1.2 if data['alcohol'] else 1.0
    
    # Fiziksel aktivite faktörü
    activity_factors = {
        'low': 1.3,
        'moderate': 1.0,
        'high': 0.8
    }
    activity_factor = activity_factors.get(data['physical_activity'], 1.0)
    
    # Toplam risk skoru (0-100 arası)
    risk_score = (
        (age_factor * 30) + 
        (gender_factor * 10) + 
        (bmi_factor * 20) + 
        (bp_factor * 15) + 
        (cholesterol_factor * 25)
    ) * smoker_factor * alcohol_factor * activity_factor
    
    # 0-100 aralığına sınırla
    risk_score = max(0, min(100, risk_score))
    
    # Risk kategorisi
    if risk_score < 20:
        risk_category = "Düşük Risk"
    elif risk_score < 50:
        risk_category = "Orta Risk"
    else:
        risk_category = "Yüksek Risk"
    
    return {
        "risk_score": round(risk_score, 2),
        "risk_category": risk_category,
        "factors": {
            "age_factor": round(age_factor, 2),
            "bmi": round(bmi, 1),
            "cholesterol_ratio": round(cholesterol_ratio, 2)
        }
    }

class HealthData(BaseModel):
    # Yaş: 0-120 arasında olmalı
    age: int = Field(..., ge=0, le=120, description="Kişinin yaşı")
    gender: Literal["male", "female"]

    # Kilo ve Boy: Pozitif olmalı
    weight: float = Field(..., gt=0, description="Kişinin kilosu (kg)")
    height: float = Field(..., gt=0, description="Kişinin boyu (cm)")

    # Tansiyon Değerleri: Makul aralıklar
    systolic_bp: int = Field(..., ge=70, le=250, description="Sistolik kan basıncı")
    diastolic_bp: int = Field(..., ge=40, le=150, description="Diyastolik kan basıncı")

    # Kolesterol Değerleri: Pozitif olmalı
    cholesterol_ldl: float = Field(..., gt=0, description="LDL Kolesterol değeri")
    cholesterol_hdl: float = Field(..., gt=0, description="HDL Kolesterol değeri")
    cholesterol_total: float = Field(..., gt=0, description="Toplam Kolesterol değeri")

    smoker: bool
    alcohol: bool
    physical_activity: Literal["low", "moderate", "high"]

    # --- Ek Validasyonlar (Sınıf Bazında) ---
    @validator('diastolic_bp')
    def validate_diastolic_bp_less_than_systolic(cls, v, values):
        """Diyastolik tansiyonun sistolik tansiyondan küçük olduğunu kontrol eder."""
        if 'systolic_bp' in values and v >= values['systolic_bp']:
            raise ValueError('Diyastolik kan basıncı, sistolik kan basıncından küçük olmalıdır.')
        return v

    @validator('cholesterol_total')
    def validate_total_cholesterol_consistency(cls, v, values):
        """Toplam kolesterolün LDL ve HDL toplamından büyük veya eşit olduğunu kontrol eder."""
        if 'cholesterol_ldl' in values and 'cholesterol_hdl' in values:
            calculated_total = values['cholesterol_ldl'] + values['cholesterol_hdl']
            # Genellikle total, LDL + HDL + VLDL'dir. Basitçe >= kontrolü yapalım.
            if v < calculated_total * 0.95: # %5'lik bir tolerans bırakılabilir
                raise ValueError('Toplam kolesterol, LDL ve HDL toplamına yakın veya ondan büyük olmalıdır.')
        return v


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/api/analyze")
async def submit_health_data(data: HealthData, db: Session = Depends(get_db)):
    # Veriyi sözlüğe çevir
    health_data = data.dict()
    
    # Risk skorunu hesapla
    risk_result = calculate_heart_disease_risk(health_data)
    
    # Veritabanına kaydet
    db_record = HealthRecord(
        **health_data,
        risk_score=risk_result["risk_score"],
        risk_category=risk_result["risk_category"]
    )
    
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    
    # Sonuçları döndür
    return {
        "message": "Analiz başarıyla tamamlandı", 
        "record_id": db_record.id,
        "risk_score": risk_result["risk_score"],
        "risk_category": risk_result["risk_category"],
        "factors": risk_result["factors"]
    }

# Tüm kayıtları getir
@app.get("/api/records", response_model=List[dict])
async def get_health_records(db: Session = Depends(get_db)):
    records = db.query(HealthRecord).order_by(HealthRecord.created_at.desc()).all()
    return [{
        "id": record.id,
        "age": record.age,
        "gender": record.gender,
        "risk_score": record.risk_score,
        "risk_category": record.risk_category,
        "created_at": record.created_at.isoformat()
    } for record in records]

# Tek bir kaydı getir
@app.get("/api/records/{record_id}")
async def get_health_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(HealthRecord).filter(HealthRecord.id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı")
    
    return {
        "id": record.id,
        "age": record.age,
        "gender": record.gender,
        "weight": record.weight,
        "height": record.height,
        "systolic_bp": record.systolic_bp,
        "diastolic_bp": record.diastolic_bp,
        "cholesterol_ldl": record.cholesterol_ldl,
        "cholesterol_hdl": record.cholesterol_hdl,
        "cholesterol_total": record.cholesterol_total,
        "smoker": record.smoker,
        "alcohol": record.alcohol,
        "physical_activity": record.physical_activity,
        "risk_score": record.risk_score,
        "risk_category": record.risk_category,
        "created_at": record.created_at.isoformat()
    }
