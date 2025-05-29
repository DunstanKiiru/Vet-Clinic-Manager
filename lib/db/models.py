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
    
    class Owner(Base):
        __tablename__ = "owners"
        
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)
        phone = Column(String)
        
        pets = relationship("Pet", back_populates="owner", cascade="all, delete")

    class Pet(Base):
        __tablename__ = "pets"
        
        id = Column(Integer, primary_key=True)
        name = Column(String)
        species = Column(String)
        breed = Column(String)
        sex = Column(String)
        color = Column(String)
        dob = Column(DateTime)
        medical_notes = Column(Text)
        
        owner_id = Column(Integer, ForeignKey("owners.id"))
        owner = relationship("Owner", back_populates="pets")

        appointments = relationship("Appointment", back_populates="pet", cascade="all, delete")
        treatments = relationship("Treatment", back_populates="pet", cascade="all, delete")
        billings = relationship("Billing", back_populates="pet", cascade="all, delete")
    
    class Appointment(Base):
        __tablename__ = "appointments"
        
        id = Column(Integer, primary_key=True)
        date = Column(DateTime)
        reason = Column(String)
        
        pet_id = Column(Integer, ForeignKey("pets.id"))
        pet = relationship("Pet", back_populates="appointments")
        
        staff_id = Column(Integer, ForeignKey("staff.id"))
        staff = relationship("Staff", back_populates="appointments")
        
    class Treatment(Base):
        __tablename__ = "treatments"
        
        id = Column(Integer, primary_key=True)
        date = Column(DateTime)
        description = Column(Text)
        
        pet_id = Column(Integer, ForeignKey("pets.id"))
        pet = relationship("Pet", back_populates="treatments")
        
        staff_id = Column(Integer, ForeignKey("staff.id"))
        staff = relationship("Staff", back_populates="treatments")
        
        medications = relationship("Medication", back_populates="treatment", cascade="all, delete")
    
    class Medication(Base):
        __tablename__ = "medications"
        
        id = Column(Integer, primary_key=True)
        name = Column(String)
        dosage = Column(String)
        frequency = Column(String)
        
        treatment_id = Column(Integer, ForeignKey("treatments.id"))
        treatment = relationship("Treatment", back_populates="medications")
    
    class Billing(Base):
        __tablename__ = "billings"
        
        id = Column(Integer, primary_key=True)
        date = Column(DateTime)
        amount = Column(Float)
        description = Column(String)
        
        pet_id = Column(Integer, ForeignKey("pets.id"))
        pet = relationship("Pet", back_populates="billings")
        