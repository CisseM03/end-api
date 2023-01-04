from sqlalchemy.orm import Session
from faker import Faker

import models
import schemas
import auth

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_id(db: Session, id: str):
    return db.query(models.User).filter(models.User.id == id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_america(db: Session, owner: schemas.AmericaCreate):
    fake = Faker('en_US')
    generated_name = fake.name()
    db_america = models.Fakeamerica(america_name=generated_name, owner_id=owner.owner_id)
    db.add(db_america)
    db.commit()
    db.refresh(db_america)
    return db_america

def get_america_by_ownerid(db: Session, ownerid: int):
    return db.query(models.Fakeamerica).filter(models.Fakeamerica.owner_id == ownerid).first()


def get_japan_by_ownerid(db: Session, ownerid: int):
    return db.query(models.Fakejapan).filter(models.Fakejapan.owner_id == ownerid).first()


def create_japan(db: Session, owner: schemas.JapanCreate):
    fake = Faker('ja_JP')
    generated_name = fake.name()
    db_japan = models.Fakejapan(japan_name=generated_name, owner_id=owner.owner_id)
    db.add(db_japan)
    db.commit()
    db.refresh(db_japan)
    return db_japan



def get_america(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fakeamerica).offset(skip).limit(limit).all()


def get_japan(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fakejapan).offset(skip).limit(limit).all()


def edit_username(db: Session, user = schemas.UserEdit, username = str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    db_user.username = user.username
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, username = str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    db.delete(db_user)
    db.commit()
    return None