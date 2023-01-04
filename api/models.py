from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    america = relationship("Fakeamerica", back_populates="owner")
    japan = relationship("Fakejapan", back_populates="owner")


class Fakeamerica(Base):
    __tablename__ = "fakeamerica"
    id = Column(Integer, primary_key=True, index=True)
    america_name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="america")

class Fakejapan(Base):
    __tablename__ = "fakejapan"
    id = Column(Integer, primary_key=True, index=True)
    japan_name = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="japan")
