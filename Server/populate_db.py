from db import SessionLocal, init_db
from models import Usuario, Transaccion

def poblar_datos():
    db = SessionLocal()
    usuarios_existentes = db.query(Usuario).count()
    if usuarios_existentes == 0:
        for i in range(1, 4):
            user = Usuario(saldo=100.0 * i)
            db.add(user)
            db.flush()
            trans = Transaccion(usuario_id=user.id, monto=50.0 * i)
            user.saldo += trans.monto
            db.add(trans)
        db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
    poblar_datos()
