from sqlalchemy import Column, Integer, String, Numeric, Date, Time, TIMESTAMP, func
from database import Base

class Ork(Base):
    __tablename__ = "ork"

    id = Column(Integer, primary_key=True, index=True)
    qurilma_id = Column(String, nullable=False)
    podstansiya = Column(String)
    liniya = Column(String)
    hisoblagich = Column(String)
    koeffisent = Column(Numeric(6,3))
    i_a = Column(Numeric(10,2))
    i_b = Column(Numeric(10,2))
    i_c = Column(Numeric(10,2))
    u_a = Column(Numeric(10,2))
    u_b = Column(Numeric(10,2))
    u_c = Column(Numeric(10,2))
    cos_f = Column(Numeric(5,3))
    aktiv_quvvat = Column(Numeric(12,3))
    reaktiv_quvvat = Column(Numeric(12,3))
    energiya_kwh = Column(Numeric(14,3))
    sana = Column(Date)
    vaqt = Column(Time)
    yozilgan_vaqt = Column(TIMESTAMP, server_default=func.now())
