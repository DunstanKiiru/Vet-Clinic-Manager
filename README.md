# Vet Clinic Manager CLI

## Project Overview

The **Vet Clinic Manager CLI** is a command-line interface (CLI) application for managing the day-to-day operations of a veterinary clinic. It provides tools to manage staff, pet owners, pets, appointments, treatments, medications, and billing records efficiently through an interactive terminal interface.

---

## Project Structure

```tree
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py

```

## Features

Staff Management: Add, list, and update clinic staff with roles and contact information.

Owner Management: Store and manage pet owner records with contact details.

Pet Management: Track pets including species, breed, medical notes, and owner associations.

Appointments: Schedule and view appointments with veterinary-relevant reasons.

Treatments: Record treatment procedures performed on pets.

Medications: Manage prescribed medications associated with treatments.

Billing: Generate billing records with descriptions for various clinic services.

Interactive CLI: Intuitive menu-based navigation to access all functionality.

## Installation

1.Clone this repository to your local machine:

<git@github.com>:DunstanKiiru/Vet-Clinic-Manager.git
2. Ensure Python 3.8+ is installed.
3. Install dependencies using Pipenv:
pipenv install sqlalchemy alembic faker tabulate

1. Activate the virtual environment:

    pipenv shell

## Database Setup

1. Initialize the database:

    python lib/cli.py and select option 1

2. From the CLI menu, select option 1 to initialize the database.

3. Seed the database with sample data by running the seed script or using CLI commands.

  python -m lib.db.seed

## Usage

Run the CLI application:

   python lib/cli.py

From the interactive CLI menu, you can:

Add or list staff members

Add or list pet owners

Register and view pets

Schedule or view appointments

Log treatments

Prescribe medications

Create and view billing records

## Demo

Welcome to Vet Clinic Manager!

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

Example Submenus:

Staff Menu:

1. Add Staff
2. List Staff
3. Delete Staff
4. Back to Main Menu

Owner Menu:

1. Add Owner
2. List Owners
3. Delete Owner
4. Back to Main Menu

Pet Menu:

1. Add Pet
2. List Pets
3. Delete Pet
4. Back to Main Menu

Appointment Menu:

1. Add Appointment
2. List Appointments
3. Back to Main Menu

Treatment Menu:

1. Add Treatment
2. List Treatments
3. Delete Treatment
4. Back to Main Menu

Medication Menu:

1. Add Medication
2. List Medications
3. Delete Medication
4. Back to Main Menu

Billing Menu:

1. Add Billing
2. List Billing
3. Update Billing Paid Status
4. Back to Main Menu

...

## Menus and Submenus

The Vet Clinic Manager CLI provides the following menus and submenus for managing the veterinary clinic operations:

- Database
  - Initialize Database

- Staff Management
  - Add Staff Member
  - List Staff Members

- Owner Management
  - Add Pet Owner
  - List Pet Owner

- Pet Management
  - Add Pet
  - List Pets

- Appointments
  - Add Appointment
  - List Appointments

- Treatments
  - Add Treatment
  - List Treatments

- Medications
  - Add Medication

- Billing
  - Add Billing
  - List Billings
  - Update Billing Paid Status

## Seed Data Updates

Billing: Includes veterinary-specific services like "Vaccination fee", "Dental cleaning", and "Surgery charge".

Treatments: Descriptions reflect real vet procedures such as "Annual physical examination" and "Vaccination administration".

Appointments: Reason fields now show options like "Routine check-up" and "Emergency visit".

Display: Treatment listings now include the pet’s name and ID for clarity.

To generate seed data for the database run
python -m lib.db.seed
from the root folder

## Contributing

I welcome contributions to improve this project! Here's how you can get involved:

1. **Fork the repository** 🍴:
   Click the "Fork" button at the top of the repo to create your own copy of the project.

2. **Create a new branch**:  
   Create a branch for your feature or fix.

   ```bash
   git checkout -b feature-name
   ```

## 3. Make your changes ✏️

Now that you've created a new branch, you can start making changes to the project. Whether it's fixing a bug, adding a feature, or updating documentation, feel free to modify the necessary files. Be sure to follow the code style and guidelines for consistency.

---

### 4. Commit your changes 📝

Once you've made your changes, commit them to your branch with a clear and descriptive commit message. This helps others understand the changes you've made.

To commit your changes:

```bash
git commit -m "Brief description of changes made"

```