from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import func
from app.dependencies import verify_api_key
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    return db.query(models.Order).all()

@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    order = db.query(models.Order).get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=schemas.OrderResponse)
def update_status(order_id: int, db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    order = db.query(models.Order).get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = "done"
    db.commit()
    db.refresh(order)
    return order

@router.get("/statistics/")
def order_statistics(db: Session = Depends(get_db), _: str = Depends(verify_api_key)):
    total = db.query(models.Order).count()
    average = db.query(func.avg(models.Order.price)).scalar()
    return {
        "total_orders": total,
        "average_price": round(average or 0, 2)
    }
