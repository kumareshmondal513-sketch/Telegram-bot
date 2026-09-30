from sqlalchemy import Column, Integer, BigInteger
from .database import Base

class User(Base):
    __tablename__ = "users"

    telegram_id = Column(BigInteger, primary_key=True, index=True)
    balance = Column(Integer, default=0)
    energy = Column(Integer, default=1000)
    max_energy = Column(Integer, default=1000)
