
# lib/cli.py

from db.models import (
    Base, engine, Session,
    Staff, Owner, Pet, Appointment,
    Treatment, Medication, Billing
)
from datetime import datetime

session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("\n✅ Database initialized!")



def input_date(prompt="Enter date (YYYY-MM-DD): "):
    date_str = input(prompt)
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format.")
        return None




def add_staff():
    print("\n➕ Add Staff")
    name = input("Name: ")
    role = input("Role: ")
    email = input("Email: ")
    phone = input("Phone: ")

    staff = Staff(name=name, role=role, email=email, phone=phone)
    session.add(staff)
    session.commit()
    print(f"✅ Staff '{name}' added.")


def list_staff():
    print("\n📋 Staff Members")
    for s in session.query(Staff).all():
        print(f"{s.id}: {s.name} ({s.role}) | {s.email} | {s.phone}")



def add_owner():
    print("\n➕ Add Owner")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    owner = Owner(name=name, email=email, phone=phone)
    session.add(owner)
    session.commit()
    print(f"✅ Owner '{name}' added.")


def list_owners():
    print("\n📋 Owners")
    for o in session.query(Owner).all():
        print(f"{o.id}: {o.name} | {o.email} | {o.phone}")



def add_pet():
    print("\n➕ Add Pet")
    name = input("Name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    sex = input("Sex: ")
    color = input("Color: ")
    dob = input_date("Date of Birth (YYYY-MM-DD): ")
    medical_notes = input("Medical Notes: ")

    list_owners()
    owner_id = int(input("Owner ID: "))
    owner = session.query(Owner).get(owner_id)

    pet = Pet(
        name=name, species=species, breed=breed, sex=sex,
        color=color, dob=dob, medical_notes=medical_notes,
        owner=owner
    )
    session.add(pet)
    session.commit()
    print(f"✅ Pet '{name}' added.")


def list_pets():
    print("\n📋 Pets")
    for p in session.query(Pet).all():
        print(f"{p.id}: {p.name} ({p.species}) - Owner: {p.owner.name}")



def add_appointment():
    print("\n➕ Add Appointment")
    list_pets()
    pet_id = int(input("Pet ID: "))
    pet = session.query(Pet).get(pet_id)

    list_staff()
    staff_id = int(input("Staff ID: "))
    staff = session.query(Staff).get(staff_id)

    date = input_date()
    reason = input("Reason: ")

    appointment = Appointment(date=date, reason=reason, pet=pet, staff=staff)
    session.add(appointment)
    session.commit()
    print("✅ Appointment added.")


def list_appointments():
    print("\n📋 Appointments")
    for a in session.query(Appointment).all():
        print(f"{a.id}: {a.date} - {a.pet.name} with {a.staff.name} ({a.reason})")


def add_treatment():
    print("\n➕ Add Treatment")
    list_pets()
    pet_id = int(input("Pet ID: "))
    pet = session.query(Pet).get(pet_id)

    list_staff()
    staff_id = int(input("Staff ID: "))
    staff = session.query(Staff).get(staff_id)

    date = input_date()
    description = input("Description: ")

    treatment = Treatment(date=date, description=description, pet=pet, staff=staff)
    session.add(treatment)
    session.commit()
    print("✅ Treatment added.")


def list_treatments():
    print("\n📋 Treatments")
    for t in session.query(Treatment).all():
        print(f"{t.id}: {t.date} - {t.pet.name} by {t.staff.name} ({t.description})")



def add_medication():
    print("\n➕ Add Medication")
    list_treatments()
    treatment_id = int(input("Treatment ID: "))
    treatment = session.query(Treatment).get(treatment_id)

    name = input("Medication Name: ")
    dosage = input("Dosage: ")
    frequency = input("Frequency: ")

    medication = Medication(name=name, dosage=dosage, frequency=frequency, treatment=treatment)
    session.add(medication)
    session.commit()
    print("✅ Medication added.")


def list_treatments():
    treatments = session.query(Treatment).all()
    print("\n📋 Treatments")
    for t in treatments:
        print(f"{t.id}: {t.date} - {t.description}")


# === BILLING ===

def add_billing():
    print("\n➕ Add Billing Record")
    list_pets()
    pet_id = int(input("Pet ID: "))
    pet = session.query(Pet).get(pet_id)

    date = input_date()
    amount = float(input("Amount: "))
    description = input("Description: ")

    billing = Billing(date=date, amount=amount, description=description, pet=pet)
    session.add(billing)
    session.commit()
    print("✅ Billing added.")


def list_billing():
    print("\n📋 Billing Records")
    for b in session.query(Billing).all():
        print(f"{b.id}: {b.date} - {b.pet.name} - ${b.amount} ({b.description})")



def menu():
    print("\n🐾 Vet Clinic CLI")
    while True:
        print("""
==============================
1. Init DB
2. Add Staff
3. List Staff
4. Add Owner
5. List Owners
6. Add Pet
7. List Pets
8. Add Appointment
9. List Appointments
10. Add Treatment
11. List Treatments
12. Add Medication
13. Add Billing
14. List Billing
15. Exit
==============================
""")
        choice = input("Choose an option: ").strip()

        if choice == '1': init_db()
        elif choice == '2': add_staff()
        elif choice == '3': list_staff()
        elif choice == '4': add_owner()
        elif choice == '5': list_owners()
        elif choice == '6': add_pet()
        elif choice == '7': list_pets()
        elif choice == '8': add_appointment()
        elif choice == '9': list_appointments()
        elif choice == '10': add_treatment()
        elif choice == '11': list_treatments()
        elif choice == '12': add_medication()
        elif choice == '13': add_billing()
        elif choice == '14': list_billing()
        elif choice == '15':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
