# lib/db/models.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///clinic.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Float

from sqlalchemy.orm import relationship, declarative_base


class Staff(Base):
    __tablename__ = "staff"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    email = Column(String)
    phone = Column(String)
    
    appointments = relationship("Appointment", back_populates="staff", cascade="all, delete")
    treatments = relationship("Treatment", back_populates="staff", cascade="all, delete")