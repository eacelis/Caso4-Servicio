from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    saldo = Column(Float, default=0.0)
    transacciones = relationship("Transaccion", back_populates="usuario")

class Transaccion(Base):
    __tablename__ = "transacciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    monto = Column(Float)

    usuario = relationship("Usuario", back_populates="transacciones")
