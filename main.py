from fastapi import FastAPI
from routers import ork
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Energiya Monitoring Backend",
    description="FastAPI backend for NMET",
    version="1.0.0"
)

# Routerni ulash
app.include_router(ork.router)

# CORS ruxsatlari (zarur frontend bilan bog‘lanish uchun)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # yoki ["https://frontend-url.vercel.app"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB bazasini yaratish
Base.metadata.create_all(bind=engine)

# Test uchun endpoint
@app.get("/")
def root():
    return {"status": "Backend ishlayapti"}

