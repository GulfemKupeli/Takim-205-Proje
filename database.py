from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite veritabanı bağlantısı
SQLALCHEMY_DATABASE_URL = "sqlite:///./kalp_sagligi.db"

# Motor oluşturma
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal sınıfı
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base sınıfı
Base = declarative_base()

# Kullanıcı sağlık verileri tablosu
class HealthRecord(Base):
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    systolic_bp = Column(Integer, nullable=False)
    diastolic_bp = Column(Integer, nullable=False)
    cholesterol_ldl = Column(Float, nullable=False)
    cholesterol_hdl = Column(Float, nullable=False)
    cholesterol_total = Column(Float, nullable=False)
    smoker = Column(Boolean, default=False)
    alcohol = Column(Boolean, default=False)
    physical_activity = Column(String, nullable=False)
    risk_score = Column(Float, nullable=True)
    risk_category = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())

# Veritabanı tablolarını oluştur
def create_tables():
    Base.metadata.create_all(bind=engine)

# Bağımlılık olarak kullanılacak veritabanı bağlantısı
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
