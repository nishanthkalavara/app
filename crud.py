from sqlalchemy.orm import Session
from sqlalchemy import or_
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_data(db: Session,  user: schemas.UserCreate):
    return db.query(models.User).filter(or_(models.User.name==user.name,models.User.url==user.url ,models.User.caption==user.caption)).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).order_by(models.User.id.desc()).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    
    db_user = models.User(name=user.name, url=user.url, caption=user.caption)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"id":db_user.id}


