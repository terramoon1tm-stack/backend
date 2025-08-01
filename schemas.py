from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class OrkCreate(BaseModel):
    qurilma_id: str
    podstansiya: str
    liniya: str
    hisoblagich: str
    i_a: float
    i_b: float
    i_c: float
    u_a: float
    u_b: float
    u_c: float
    cos_f: float
    aktiv_quvvat: float
    reaktiv_quvvat: float
    energiya_kwh: float
    sana: date
    vaqt: time

