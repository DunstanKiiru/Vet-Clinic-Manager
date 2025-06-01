from faker import Faker
from datetime import datetime, timedelta
import random
import traceback

from lib.db.models import engine, Session, Base
from lib.db.models import Staff, Owner, Pet, Appointment, Treatment, Medication, Billing

fake = Faker()

def drop_and_create_all():
    print("Dropping and creating tables...")
    try:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        print("Tables created.")
    except Exception as e:
        print(f"Error during drop and create tables: {e}")
        traceback.print_exc()

def seed_staff(session, n=5):
    staff_list = []
    roles = ['Vet', 'vet', 'vet', 'vet']
    try:
        for _ in range(n):
            staff = Staff(
                name=fake.name(),
                role=random.choice(roles),
                email=fake.unique.email(),
                phone=fake.phone_number()
            )
            staff_list.append(staff)
        session.add_all(staff_list)
        session.commit()
        print(f"Seeded {n} staff")
    except Exception as e:
        print(f"Error seeding staff: {e}")
        traceback.print_exc()
    return staff_list

def seed_owners(session, n=10):
    owner_list = []
    try:
        for _ in range(n):
            owner = Owner(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.phone_number()
            )
            owner_list.append(owner)
        session.add_all(owner_list)
        session.commit()
        print(f"Seeded {n} owners")
    except Exception as e:
        print(f"Error seeding owners: {e}")
        traceback.print_exc()
    return owner_list

def seed_pets(session, owners, n=20):
    species_list = ['Dog', 'Cat', 'Bird', 'Rabbit', 'Hamster']
    breeds = {
        'Dog': ['Labrador Retriever', 'German Shepherd', 'Golden Retriever', 'Bulldog', 'Beagle'],
        'Cat': ['Siamese', 'Persian', 'Maine Coon', 'Ragdoll', 'Sphynx'],
        'Bird': ['Parakeet', 'Canary', 'Finch', 'Cockatiel', 'Lovebird'],
        'Rabbit': ['Holland Lop', 'Netherland Dwarf', 'Flemish Giant', 'Lionhead', 'Mini Rex'],
        'Hamster': ['Syrian', 'Dwarf Campbell', 'Roborovski', 'Chinese', 'Winter White']
    }
    medical_notes_samples = [
        "Healthy and active.",
        "Requires special diet due to allergies.",
        "Recently vaccinated and in good health.",
        "Shows signs of anxiety during visits.",
        "Has a mild skin condition, under treatment.",
        "Regularly takes prescribed medication.",
        "Needs dental checkup soon.",
        "Recovering from minor surgery.",
        "Prone to seasonal allergies.",
        "Very friendly and social."
    ]
    pet_list = []
    try:
        for _ in range(n):
            species = random.choice(species_list)
            dob = fake.date_between(start_date='-10y', end_date='-1y')
            breed = random.choice(breeds[species])
            medical_note = random.choice(medical_notes_samples) if random.random() < 0.7 else None
            pet = Pet(
                name=fake.first_name(),
                species=species,
                breed=breed,
                sex=random.choice(['Male', 'Female']),
                color=fake.color_name(),
                dob=dob,
                medical_notes=medical_note,
                owner_id=random.choice(owners).id
            )
            pet_list.append(pet)
        session.add_all(pet_list)
        session.commit()
        print(f"Seeded {n} pets")
    except Exception as e:
        print(f"Error seeding pets: {e}")
        traceback.print_exc()
    return pet_list

def seed_appointments(session, pets, staff, n=30):
    appointment_reasons = [
        "Routine check-up",
        "Vaccination appointment",
        "Dental cleaning",
        "Surgery consultation",
        "Wound examination",
        "Parasite screening",
        "Blood test",
        "X-ray examination",
        "Medication refill",
        "Follow-up visit",
        "Emergency visit",
        "Spaying/Neutering consultation",
        "Behavioral consultation",
        "Nutritional advice",
        "Physical therapy session"
    ]
    appointments = []
    try:
        for _ in range(n):
            date = fake.date_time_between(start_date='-1y', end_date='+1y')
            reason = random.choice(appointment_reasons)
            appointment = Appointment(
                date=date,
                reason=reason,
                pet_id=random.choice(pets).id,
                staff_id=random.choice(staff).id
            )
            appointments.append(appointment)
        session.add_all(appointments)
        session.commit()
        print(f"Seeded {n} appointments")
    except Exception as e:
        print(f"Error seeding appointments: {e}")
        traceback.print_exc()
    return appointments

def seed_treatments(session, pets, staff, n=30):
    treatment_descriptions = [
        "Annual physical examination",
        "Vaccination administration",
        "Dental cleaning procedure",
        "Minor surgical procedure",
        "Wound treatment and dressing",
        "Parasite control treatment",
        "Blood test analysis",
        "X-ray imaging session",
        "Medication prescription",
        "Follow-up consultation",
        "Emergency care treatment",
        "Spaying/Neutering surgery",
        "Behavioral assessment",
        "Nutritional counseling",
        "Physical therapy session"
    ]
    treatments = []
    try:
        for _ in range(n):
            date = fake.date_between(start_date='-1y', end_date='today')
            description = random.choice(treatment_descriptions)
            treatment = Treatment(
                date=date,
                description=description,
                pet_id=random.choice(pets).id,
                staff_id=random.choice(staff).id
            )
            treatments.append(treatment)
        session.add_all(treatments)
        session.commit()
        print(f"Seeded {n} treatments")
    except Exception as e:
        print(f"Error seeding treatments: {e}")
        traceback.print_exc()
    return treatments

def seed_medications(session, treatments, n=40):
    meds = []
    med_names = ['Antibiotic', 'Painkiller', 'Vaccine', 'Vitamin', 'Antifungal']
    try:
        for _ in range(n):
            medication = Medication(
                name=random.choice(med_names),
                dosage=f"{random.randint(1, 500)} mg",
                frequency=random.choice(['Once daily', 'Twice daily', 'Every 8 hours', 'As needed']),
                treatment_id=random.choice(treatments).id
            )
            meds.append(medication)
        session.add_all(meds)
        session.commit()
        print(f"Seeded {n} medications")
    except Exception as e:
        print(f"Error seeding medications: {e}")
        traceback.print_exc()
    return meds

def seed_billings(session, pets, n=30):
    billing_descriptions = [
        "Vaccination fee",
        "Dental cleaning",
        "Surgery charge",
        "Medication cost",
        "Consultation fee",
        "X-ray imaging",
        "Lab tests",
        "Microchipping",
        "Grooming service",
        "Emergency care",
        "Hospitalization fee",
        "Spaying/Neutering",
        "Parasite treatment",
        "Follow-up visit",
        "Anesthesia charge"
    ]
    billings = []
    try:
        for _ in range(n):
            date = fake.date_between(start_date='-1y', end_date='today')
            amount = round(random.uniform(20, 500), 2)
            description = random.choice(billing_descriptions)
            billing = Billing(
                date=date,
                amount=amount,
                description=description,
                pet_id=random.choice(pets).id
            )
            billings.append(billing)
        session.add_all(billings)
        session.commit()
        print(f"Seeded {n} billings")
    except Exception as e:
        print(f"Error seeding billings: {e}")
        traceback.print_exc()
    return billings

def seed():
    session = Session()
    try:
        drop_and_create_all()
        staff = seed_staff(session)
        owners = seed_owners(session)
        pets = seed_pets(session, owners)
        appointments = seed_appointments(session, pets, staff)
        treatments = seed_treatments(session, pets, staff)
        medications = seed_medications(session, treatments)
        billings = seed_billings(session, pets)
        print("All data seeded successfully.")
    except Exception as e:
        print(f"Error during seeding process: {e}")
        traceback.print_exc()
    finally:
        session.close()

if __name__ == "__main__":
    seed()
