from db.models import (
    Base, engine, Session,
    Staff, Owner, Pet, Appointment,
    Treatment, Medication, Billing
)
from datetime import datetime
from tabulate import tabulate

session = Session()

def init_db():
    Base.metadata.create_all(engine)
    print("\nDatabase initialized!")

def input_date(prompt="Enter date (YYYY-MM-DD): "):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Please try again.")

def add_staff():
    print("\nAdd Staff")
    name = input("Name: ")
    role = input("Role: ")
    email = input("Email: ")
    phone = input("Phone: ")

    staff = Staff(name=name, role=role, email=email, phone=phone)
    session.add(staff)
    session.commit()
    print(f"Staff '{name}' added.")

def list_staff():
    print("\nStaff Members")
    staff_list = []
    for s in session.query(Staff).all():
        staff_list.append([s.id, s.name, s.role, s.email, s.phone])
    print(tabulate(staff_list, headers=["ID", "Name", "Role", "Email", "Phone"], tablefmt="grid"))

def add_owner():
    print("\nAdd Owner")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    owner = Owner(name=name, email=email, phone=phone)
    session.add(owner)
    session.commit()
    print(f"Owner '{name}' added.")

def list_owners():
    print("\nOwners")
    owner_list = []
    for o in session.query(Owner).all():
        owner_list.append([o.id, o.name, o.email, o.phone])
    print(tabulate(owner_list, headers=["ID", "Name", "Email", "Phone"], tablefmt="grid"))

def add_pet():
    print("\nAdd Pet")
    name = input("Name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    sex = input("Sex: ")
    color = input("Color: ")
    dob = input_date("Date of Birth (YYYY-MM-DD): ")
    medical_notes = input("Medical Notes: ")

    list_owners()
    while True:
        try:
            owner_id = int(input("Owner ID: "))
            owner = session.get(Owner, owner_id)  # <-- fixed here
            if owner is None:
                print("Owner not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Owner ID.")

    pet = Pet(
        name=name, species=species, breed=breed, sex=sex,
        color=color, dob=dob, medical_notes=medical_notes,
        owner=owner
    )
    session.add(pet)
    session.commit()
    print(f"Pet '{name}' added.")

def list_pets():
    print("\nPets")
    pet_list = []
    for p in session.query(Pet).all():
        pet_list.append([p.id, p.name, p.species, p.owner.name])
    print(tabulate(pet_list, headers=["ID", "Name", "Species", "Owner"], tablefmt="grid"))

def add_appointment():
    print("\nAdd Appointment")
    list_pets()
    while True:
        try:
            pet_id = int(input("Pet ID: "))
            pet = session.get(Pet, pet_id)  # <-- fixed here
            if pet is None:
                print("Pet not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Pet ID.")

    list_staff()
    while True:
        try:
            staff_id = int(input("Staff ID: "))
            staff = session.get(Staff, staff_id)  # <-- fixed here
            if staff is None:
                print("Staff not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Staff ID.")

    date = input_date()
    reason = input("Reason: ")

    appointment = Appointment(date=date, reason=reason, pet=pet, staff=staff)
    session.add(appointment)
    session.commit()
    print("Appointment added.")

def list_appointments():
    print("\nAppointments")
    appointment_list = []
    for a in session.query(Appointment).all():
        appointment_list.append([a.id, a.date.strftime("%Y-%m-%d"), a.pet.name, a.staff.name, a.reason])
    print(tabulate(appointment_list, headers=["ID", "Date", "Pet", "Staff", "Reason"], tablefmt="grid"))

def add_treatment():
    print("\nAdd Treatment")
    list_pets()
    while True:
        try:
            pet_id = int(input("Pet ID: "))
            pet = session.get(Pet, pet_id)  # <-- fixed here
            if pet is None:
                print("Pet not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Pet ID.")

    list_staff()
    while True:
        try:
            staff_id = int(input("Staff ID: "))
            staff = session.get(Staff, staff_id)  # <-- fixed here
            if staff is None:
                print("Staff not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Staff ID.")

    date = input_date()
    description = input("Description: ")

    treatment = Treatment(date=date, description=description, pet=pet, staff=staff)
    session.add(treatment)
    session.commit()
    print("Treatment added.")

def list_treatments():
    print("\nTreatments")
    treatment_list = []
    for t in session.query(Treatment).all():
        treatment_list.append([t.id, t.date.strftime("%Y-%m-%d"), t.pet.name, t.staff.name, t.description])
    print(tabulate(treatment_list, headers=["ID", "Date", "Pet", "Staff", "Description"], tablefmt="grid"))

def add_medication():
    print("\nAdd Medication")
    list_treatments()
    while True:
        try:
            treatment_id = int(input("Treatment ID: "))
            treatment = session.get(Treatment, treatment_id)  # <-- fixed here
            if treatment is None:
                print("Treatment not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Treatment ID.")

    name = input("Medication Name: ")
    dosage = input("Dosage: ")
    frequency = input("Frequency: ")

    medication = Medication(name=name, dosage=dosage, frequency=frequency, treatment=treatment)
    session.add(medication)
    session.commit()
    print("Medication added.")

def add_billing():
    print("\nAdd Billing Record")
    list_pets()
    while True:
        try:
            pet_id = int(input("Pet ID: "))
            pet = session.get(Pet, pet_id)  # <-- fixed here
            if pet is None:
                print("Pet not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Pet ID.")

    date = input_date()
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    description = input("Description: ")

    billing = Billing(date=date, amount=amount, description=description, pet=pet)
    session.add(billing)
    session.commit()
    print("Billing added.")

def list_billing():
    print("\nBilling Records")
    billing_list = []
    for b in session.query(Billing).all():
        billing_list.append([b.id, b.date.strftime("%Y-%m-%d"), b.pet.name, b.amount, b.description])
    print(tabulate(billing_list, headers=["ID", "Date", "Pet", "Amount", "Description"], tablefmt="grid"))


def menu():
    print("\nVet Clinic CLI")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()
