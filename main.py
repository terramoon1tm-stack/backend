from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 🔥 muhim!

from database import Base, engine
from routers import ork

app = FastAPI(
    title="Energiya Monitoring Tizimi",
    description="FastAPI backend",
    version="1.0"
)

# 🔐 CORS ruxsatini qo‘shamiz:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # yoki ["http://localhost:5173"] — frontend uchun
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Bazani yaratish
Base.metadata.create_all(bind=engine)

# Routerni ulash
app.include_router(ork.router)

# Test endpoint
@app.get("/")
def index():
    return {"status": "Backend ishlayapti"}
