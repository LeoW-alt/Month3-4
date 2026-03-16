## Month3-4
# CONTACT MANAGER CLI APP
A simple command-line contact management application written in Python. Contacts are stored in a local JSON file so your data persists between sessions.

---

## Features

- Add new contacts with name, phone number, and email
- List all saved contacts (sorted alphabetically)
- Edit an existing contact's name, phone, or email
- Delete a contact with a confirmation prompt
- Search contacts by name, phone, or email
- Input validation for phone numbers and email addresses
- Persistent storage via a local `contacts.json` file

---

## Requirements

- Python 3.x (no external libraries required)

---

## Getting Started

1. Clone or download the repository.
2. Run the app from your terminal:

## Usage

On launch you'll see the main menu:

```
  ------------------------
 |     Contact Manager    |
 |------------------------|
 |1. List all contacts    |
 |2. Add contact          |
 |3. Edit contact         |
 |4.Delete contact        |
 |5.Search contacts       |
  ------------------------
```

Enter a number to select an option, or `0` to exit.

### 1. List All Contacts
Displays all saved contacts sorted alphabetically, showing name, phone, and email.

### 2. Add a Contact
Enter a name, phone number, and email address. The name is normalized to title case (e.g. `john doe` → `John Doe`). Duplicate names are not allowed.

### 3. Edit a Contact
Look up a contact by name and update any combination of their name, phone, or email. Press Enter on any field to keep the current value.

### 4. Delete a Contact
Look up a contact by name. You'll be asked to confirm before the contact is permanently removed.

### 5. Search Contacts
Enter any search term to find contacts matching by name, phone number, or email address.

### 0. Exit
Exits the application.

---

## Data Storage

Contacts are stored in a `contacts.json` file in the same directory as the script. Each contact is keyed by their normalized name:

```json
{
  "Leone": {
    "phone": "+256 700 123456",
    "email": "leone@example.com"
  }
}
```

The file is created automatically and updated after every add, edit, or delete.

---

## Input Validation

| Field | Rules |
|-------|-------|
| Name  | Cannot be empty |
| Phone | Digits only (after stripping `+`, `-`, spaces, parentheses); must be 7–15 digits |
| Email | Must contain `@` and a `.` in the domain |

---
