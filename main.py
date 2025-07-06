from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, validator, Field, ValidationError
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

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


@app.post("/submit-health-data")
async def submit_health_data(data: HealthData):
    # Geçici olarak basit bir kontrol: yüksek tansiyon veya sigara varsa risk yüksek
    high_risk = data.systolic_bp > 140 or data.smoker or data.cholesterol_total > 240
    risk = "Yüksek Risk" if high_risk else "Düşük Risk"
    return {"risk_level": risk, "received_data": data}
