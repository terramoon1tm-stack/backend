from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import OrkCreate
from crud import create_ork
import psycopg2
from models import Ork

router = APIRouter(prefix="/api", tags=["Ork"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST: ORK yozuvi qo‘shish
@router.post("/ork")
def insert_ork(data: OrkCreate, db: Session = Depends(get_db)):
    conn = psycopg2.connect(
        dbname='nmet',
        user='postgres',
        password='0076',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT koeffisent FROM hisoblagichlar
        WHERE podstansiya=%s AND liniya=%s AND hisoblagich=%s
    """, (data.podstansiya, data.liniya, data.hisoblagich))
    result = cur.fetchone()
    conn.close()

    if result is None:
        raise HTTPException(status_code=404, detail="Koeffisent topilmadi")

    koeffisent = result[0]
    return create_ork(db=db, data=data, koeffisent=koeffisent)

# GET 1: Podstansiyalar ro‘yxati
@router.get("/podstansiyalar")
def get_podstansiyalar():
    conn = psycopg2.connect(
        dbname='nmet',
        user='postgres',
        password='0076',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT podstansiya FROM hisoblagichlar")
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]

# GET 2: Liniyalar (podstansiyaga qarab)
@router.get("/liniyalar")
def get_liniyalar(podstansiya: str = Query(...)):
    conn = psycopg2.connect(
        dbname='nmet',
        user='postgres',
        password='0076',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT liniya FROM hisoblagichlar WHERE podstansiya = %s", (podstansiya,))
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]

# GET 3: Hisoblagichlar (podstansiya + liniya)
@router.get("/hisoblagichlar")
def get_hisoblagichlar(podstansiya: str = Query(...), liniya: str = Query(...)):
    conn = psycopg2.connect(
        dbname='nmet',
        user='postgres',
        password='0076',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT DISTINCT hisoblagich FROM hisoblagichlar 
        WHERE podstansiya = %s AND liniya = %s
    """, (podstansiya, liniya))
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]

# GET 4: Koeffisent (hisoblagich orqali)
@router.get("/koeffisent")
def get_koeffisent(hisoblagich: str = Query(...)):
    conn = psycopg2.connect(
        dbname='nmet',
        user='postgres',
        password='0076',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    cur.execute("SELECT koeffisent FROM hisoblagichlar WHERE hisoblagich = %s", (hisoblagich,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return 0.0

# GET 5: Barcha ORK yozuvlarini olish (jadvalni ko‘rsatish uchun)
@router.get("/orklar")
def get_all_orklar(db: Session = Depends(get_db)):
    return db.query(Ork).order_by(Ork.yozilgan_vaqt.desc()).all()
