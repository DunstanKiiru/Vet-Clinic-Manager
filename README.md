# Vet Clinic Manager

This is a CLI-based application for managing a veterinary clinic's database, including staff, owners, pets, appointments, treatments, medications, and billing.

## New Feature: Confirmation Prompt Before CRUD Operations

Before performing any Create, Update, or Delete (CRUD) operations on the database tables, the application now prompts the user for confirmation with a yes/no alert. This helps prevent accidental modifications or deletions.

### Behavior

- When adding a new record (e.g., staff, owner, pet, appointment, treatment, medication, billing), the user is asked to confirm the action before it is committed.
- When deleting a record, the user is asked to confirm the deletion before it proceeds.
- When updating a billing payment status, the user is asked to confirm the update before it is applied.
- If the user answers "no" or "n" to the confirmation prompt, the operation is cancelled gracefully with a message "Operation cancelled."

This feature improves the safety and usability of the CLI application by reducing unintended data changes.

## Usage

Run the CLI as usual. When performing CRUD operations, respond to the confirmation prompts accordingly.
