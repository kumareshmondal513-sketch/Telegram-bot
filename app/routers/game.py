
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["game"])

class TapRequest(BaseModel):
    telegram_id: int
    taps: int

@router.get("/user/{telegram_id}")
def get_user_data(telegram_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

@router.post("/tap")
def process_tap(request: TapRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.telegram_id == request.telegram_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.energy < request.taps:
        raise HTTPException(status_code=400, detail="Not enough energy")
    
    user.balance += request.taps
    user.energy -= request.taps
    db.commit()
    db.refresh(user)
    
    return {"balance": user.balance, "energy": user.energy}
