from sqlalchemy import Column, Integer, String
from app.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id: int = Column(Integer, primary_key=True)
    address: str = Column(String)
