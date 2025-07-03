from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gerekirse değiştir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class HealthData(BaseModel):
    age: int
    gender: Literal["male", "female"]
    weight: float
    height: float
    systolic_bp: int
    diastolic_bp: int
    cholesterol_ldl: float
    cholesterol_hdl: float
    cholesterol_total: float
    smoker: bool
    alcohol: bool
    physical_activity: Literal["low", "moderate", "high"]


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/submit-health-data")
async def submit_health_data(data: HealthData):
    # Geçici olarak basit bir kontrol: yüksek tansiyon veya sigara varsa risk yüksek
    high_risk = data.systolic_bp > 140 or data.smoker or data.cholesterol_total > 240
    risk = "Yüksek Risk" if high_risk else "Düşük Risk"
    return {"risk_level": risk, "received_data": data}
