# lib/db/seed.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.models import (
    Base, engine, Session,
    Staff, Owner, Pet, Appointment, Treatment, Medication, Billing
)

from sqlalchemy.exc import IntegrityError

session = Session()

def reset_database():
    print("Creating tables...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def seed_data():
    # Add sample owners
    owner1 = Owner(name="Alice Johnson", contact="alice@example.com")
    owner2 = Owner(name="Bob Smith", contact="bob@example.com")

    # Add sample pets
    pet1 = Pet(name="Max", species="Dog", breed="Labrador", sex="Male", color="Black", dob="2019-06-15", owner=owner1)
    pet2 = Pet(name="Whiskers", species="Cat", breed="Siamese", sex="Female", color="White", dob="2020-03-10", owner=owner2)

    # Add sample staff
    staff1 = Staff(name="Dr. Jane", role="Vet")
    staff2 = Staff(name="Mark Lee", role="Receptionist")

    # Add everything to the session
    session.add_all([owner1, owner2, pet1, pet2, staff1, staff2])
    try:
        session.commit()
        print("Database seeded successfully.")
    except IntegrityError:
        session.rollback()
        print("Seeding failed due to integrity error.")

if __name__ == "__main__":
    reset_database()
    seed_data()
