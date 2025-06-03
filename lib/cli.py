from db.models import (
    Base, engine, Session,
    Staff, Owner, Pet, Appointment,
    Treatment, Medication, Billing
)
from datetime import datetime
from tabulate import tabulate

session = Session()

def confirm_action(message):
    while True:
        choice = input(f"{message} (yes/no): ").strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

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

# Staff functions
def add_staff():
    print("\nAdd Staff")
    name = input("Name: ")
    role = input("Role: ")
    email = input("Email: ")
    phone = input("Phone: ")

    staff = Staff(name=name, role=role, email=email, phone=phone)
    if confirm_action(f"Are you sure you want to add staff '{name}'?"):
        session.add(staff)
        session.commit()
        print(f"Staff '{name}' added.")
    else:
        print("Operation cancelled.")

def list_staff():
    print("\nStaff Members")
    staff_list = []
    for s in session.query(Staff).all():
        staff_list.append([s.id, s.name, s.role, s.email, s.phone])
    print(tabulate(staff_list, headers=["ID", "Name", "Role", "Email", "Phone"], tablefmt="grid"))

def delete_staff():
    print("\nDelete Staff")
    list_staff()
    while True:
        try:
            staff_id = int(input("Enter Staff ID to delete: "))
            staff = session.get(Staff, staff_id)
            if staff is None:
                print("Staff not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Staff ID.")
    if confirm_action(f"Are you sure you want to delete staff ID {staff_id}?"):
        session.delete(staff)
        session.commit()
        print(f"Staff ID {staff_id} and related records deleted.")
    else:
        print("Operation cancelled.")

def staff_menu():
    while True:
        print("""
Staff Menu:
1. Add Staff
2. List Staff
3. Delete Staff
4. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_staff()
        elif choice == '2':
            list_staff()
        elif choice == '3':
            delete_staff()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# Owner functions
def add_owner():
    print("\nAdd Owner")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    owner = Owner(name=name, email=email, phone=phone)
    if confirm_action(f"Are you sure you want to add owner '{name}'?"):
        session.add(owner)
        session.commit()
        print(f"Owner '{name}' added.")
    else:
        print("Operation cancelled.")

def list_owners():
    print("\nOwners")
    owner_list = []
    for o in session.query(Owner).all():
        owner_list.append([o.id, o.name, o.email, o.phone])
    print(tabulate(owner_list, headers=["ID", "Name", "Email", "Phone"], tablefmt="grid"))

def delete_owner():
    print("\nDelete Owner")
    list_owners()
    while True:
        try:
            owner_id = int(input("Enter Owner ID to delete: "))
            owner = session.get(Owner, owner_id)
            if owner is None:
                print("Owner not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Owner ID.")
    if confirm_action(f"Are you sure you want to delete owner ID {owner_id}?"):
        session.delete(owner)
        session.commit()
        print(f"Owner ID {owner_id} and related pets deleted.")
    else:
        print("Operation cancelled.")

def owner_menu():
    while True:
        print("""
Owner Menu:
1. Add Owner
2. List Owners
3. Delete Owner
4. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_owner()
        elif choice == '2':
            list_owners()
        elif choice == '3':
            delete_owner()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# Pet functions
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
            owner = session.get(Owner, owner_id)
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
    if confirm_action(f"Are you sure you want to add pet '{name}'?"):
        session.add(pet)
        session.commit()
        print(f"Pet '{name}' added.")
    else:
        print("Operation cancelled.")

def list_pets():
    print("\nPets")
    pet_list = []
    for p in session.query(Pet).all():
        pet_list.append([p.id, p.name, p.species, p.owner.name])
    print(tabulate(pet_list, headers=["ID", "Name", "Species", "Owner"], tablefmt="grid"))

def delete_pet():
    print("\nDelete Pet")
    list_pets()
    while True:
        try:
            pet_id = int(input("Enter Pet ID to delete: "))
            pet = session.get(Pet, pet_id)
            if pet is None:
                print("Pet not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Pet ID.")
    if confirm_action(f"Are you sure you want to delete pet ID {pet_id}?"):
        session.delete(pet)
        session.commit()
        print(f"Pet ID {pet_id} and related records deleted.")
    else:
        print("Operation cancelled.")

def pet_menu():
    while True:
        print("""
Pet Menu:
1. Add Pet
2. List Pets
3. Delete Pet
4. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_pet()
        elif choice == '2':
            list_pets()
        elif choice == '3':
            delete_pet()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# Appointment functions
def add_appointment():
    print("\nAdd Appointment")
    list_pets()
    while True:
        try:
            pet_id = int(input("Pet ID: "))
            pet = session.get(Pet, pet_id)
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
            staff = session.get(Staff, staff_id)
            if staff is None:
                print("Staff not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Staff ID.")

    date = input_date()
    reason = input("Reason: ")

    appointment = Appointment(date=date, reason=reason, pet=pet, staff=staff)
    if confirm_action("Are you sure you want to add this appointment?"):
        session.add(appointment)
        session.commit()
        print("Appointment added.")
    else:
        print("Operation cancelled.")

def list_appointments():
    print("\nAppointments")
    appointment_list = []
    for a in session.query(Appointment).all():
        appointment_list.append([a.id, a.date.strftime("%Y-%m-%d"), a.pet.name, a.staff.name, a.reason])
    print(tabulate(appointment_list, headers=["ID", "Date", "Pet", "Staff", "Reason"], tablefmt="grid"))

def appointment_menu():
    while True:
        print("""
Appointment Menu:
1. Add Appointment
2. List Appointments
3. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_appointment()
        elif choice == '2':
            list_appointments()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

# Treatment functions
def add_treatment():
    print("\nAdd Treatment")
    list_pets()
    while True:
        try:
            pet_id = int(input("Pet ID: "))
            pet = session.get(Pet, pet_id)
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
            staff = session.get(Staff, staff_id)
            if staff is None:
                print("Staff not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Staff ID.")

    date = input_date()
    description = input("Description: ")

    treatment = Treatment(date=date, description=description, pet=pet, staff=staff)
    if confirm_action("Are you sure you want to add this treatment?"):
        session.add(treatment)
        session.commit()
        print("Treatment added.")
    else:
        print("Operation cancelled.")

def list_treatments():
    print("\nTreatments")
    treatment_list = []
    for t in session.query(Treatment).all():
        treatment_list.append([t.id, t.date.strftime("%Y-%m-%d"), t.pet.name, t.staff.name, t.description])
    print(tabulate(treatment_list, headers=["ID", "Date", "Pet", "Staff", "Description"], tablefmt="grid"))

def delete_treatment():
    print("\nDelete Treatment")
    list_treatments()
    while True:
        try:
            treatment_id = int(input("Enter Treatment ID to delete: "))
            treatment = session.get(Treatment, treatment_id)
            if treatment is None:
                print("Treatment not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Treatment ID.")
    if confirm_action(f"Are you sure you want to delete treatment ID {treatment_id}?"):
        session.delete(treatment)
        session.commit()
        print(f"Treatment ID {treatment_id} and related medications deleted.")
    else:
        print("Operation cancelled.")

def treatment_menu():
    while True:
        print("""
Treatment Menu:
1. Add Treatment
2. List Treatments
3. Delete Treatment
4. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_treatment()
        elif choice == '2':
            list_treatments()
        elif choice == '3':
            delete_treatment()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# Medication functions
def add_medication():
    print("\nAdd Medication")
    list_treatments()
    while True:
        try:
            treatment_id = int(input("Treatment ID: "))
            treatment = session.get(Treatment, treatment_id)
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
    if confirm_action(f"Are you sure you want to add medication '{name}'?"):
        session.add(medication)
        session.commit()
        print("Medication added.")
    else:
        print("Operation cancelled.")

def list_medications():
    print("\nMedications")
    medication_list = []
    for m in session.query(Medication).all():
        medication_list.append([m.id, m.name, m.dosage, m.frequency, m.treatment.id])
    print(tabulate(medication_list, headers=["ID", "Name", "Dosage", "Frequency", "Treatment ID"], tablefmt="grid"))

def delete_medication():
    print("\nDelete Medication")
    list_medications()
    while True:
        try:
            medication_id = int(input("Enter Medication ID to delete: "))
            medication = session.get(Medication, medication_id)
            if medication is None:
                print("Medication not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Medication ID.")
    if confirm_action(f"Are you sure you want to delete medication ID {medication_id}?"):
        session.delete(medication)
        session.commit()
        print(f"Medication ID {medication_id} deleted.")
    else:
        print("Operation cancelled.")

def medication_menu():
    while True:
        print("""
Medication Menu:
1. Add Medication
2. List Medications
3. Delete Medication
4. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_medication()
        elif choice == '2':
            list_medications()
        elif choice == '3':
            delete_medication()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# Billing functions
def add_billing():
    print("\nAdd Billing Record")
    list_pets()
    while True:
        try:
            pet_id = int(input("Pet ID: "))
            pet = session.get(Pet, pet_id)
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
    if confirm_action("Are you sure you want to add this billing record?"):
        session.add(billing)
        session.commit()
        print("Billing added.")
    else:
        print("Operation cancelled.")

def list_billing():
    print("\nBilling Records")
    billing_list = []
    for b in session.query(Billing).all():
        billing_list.append([b.id, b.date.strftime("%Y-%m-%d"), b.pet.name, b.amount, b.description, b.paid])
    print(tabulate(billing_list, headers=["ID", "Date", "Pet", "Amount", "Description", "Paid"], tablefmt="grid"))

def update_billing_paid():
    print("\nUpdate Billing Payment Status")
    list_billing()
    while True:
        try:
            billing_id = int(input("Enter Billing ID to mark as paid: "))
            billing = session.get(Billing, billing_id)
            if billing is None:
                print("Billing record not found. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid Billing ID.")
    if confirm_action(f"Are you sure you want to mark billing ID {billing_id} as paid?"):
        billing.paid = True
        session.commit()
        print(f"Billing ID {billing_id} marked as paid.")
    else:
        print("Operation cancelled.")

def billing_menu():
    while True:
        print("""
Billing Menu:
1. Add Billing
2. List Billing
3. Update Billing Paid Status
4. Back to Main Menu
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_billing()
        elif choice == '2':
            list_billing()
        elif choice == '3':
            update_billing_paid()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("""
Main Menu:
1. Initialize Database
2. Staff Menu
3. Owners Menu
4. Pets Menu
5. Appointments Menu
6. Treatments Menu
7. Medications Menu
8. Billings Menu
9. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            init_db()
        elif choice == '2':
            staff_menu()
        elif choice == '3':
            owner_menu()
        elif choice == '4':
            pet_menu()
        elif choice == '5':
            appointment_menu()
        elif choice == '6':
            treatment_menu()
        elif choice == '7':
            medication_menu()
        elif choice == '8':
            billing_menu()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()
