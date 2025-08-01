from sqlalchemy.orm import Session
from models import Ork
from schemas import OrkCreate

def create_ork(db: Session, data: OrkCreate, koeffisent: float):
    new_record = Ork(
        qurilma_id=data.qurilma_id,
        podstansiya=data.podstansiya,
        liniya=data.liniya,
        hisoblagich=data.hisoblagich,
        koeffisent=koeffisent,
        i_a=data.i_a,
        i_b=data.i_b,
        i_c=data.i_c,
        u_a=data.u_a,
        u_b=data.u_b,
        u_c=data.u_c,
        cos_f=data.cos_f,
        aktiv_quvvat=data.aktiv_quvvat,
        reaktiv_quvvat=data.reaktiv_quvvat,
        energiya_kwh=data.energiya_kwh,
        sana=data.sana,
        vaqt=data.vaqt
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record


