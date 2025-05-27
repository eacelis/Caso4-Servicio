from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import SessionLocal, init_db
from models import Usuario, Transaccion
import populate_db

app = FastAPI()

init_db()
populate_db.poblar_datos()

class TransaccionIn(BaseModel):
    usuario_id: int
    monto: float

@app.get("/saldo/{usuario_id}")
def obtener_saldo(usuario_id: int):
    db = SessionLocal()
    user = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    db.close()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"usuario_id": user.id, "saldo": user.saldo}

@app.post("/transaccion")
def agregar_transaccion(data: TransaccionIn):
    db = SessionLocal()
    user = db.query(Usuario).filter(Usuario.id == data.usuario_id).first()
    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    trans = Transaccion(usuario_id=user.id, monto=data.monto)
    user.saldo += data.monto
    db.add(trans)
    db.commit()
    db.refresh(user)
    db.close()
    return {"mensaje": "Transacción agregada", "nuevo_saldo": user.saldo}
