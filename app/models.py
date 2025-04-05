from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    drink_name = Column(String, nullable=False)
    size = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="in progress")
