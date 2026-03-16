"""
Command line application for basic contact management
"""

import json
import os
import re

CONTACTS_FILE = "contacts.json"

#File I/O

def load_contacts():
    #Loads contacts from file
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)
    
#Saves contacts to file    
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)
    print("**Contacts saved**")

#Validation
def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]

def validate_phone(phone):
    digits = phone.replace("+", "").replace("-", "").replace(" ", "").replace("(", "").replace(")", "")
    return digits.isdigit() and 7 <= len(digits) <= 15  

def normalize_name(name):
    return name.strip().title()

def print_contact(name, info, index=None):
    prefix = f"[{index}] " if index is not None else ""
    print(f"\n  {prefix} {name}")
    print(f"        {info['phone']}")
    print(f"         {info['email']}")

#Input prompt with optional validation
def prompt(label, required=True, validator=None, hint=""):
    while True:
        value = input(f"  {label}{' (' + hint +')' if hint else ''}:").strip()
        if not value:
            if not required:
                return value
            print(f"  {label} cannot be empty.")
            continue
        if validator and not validator(value):
            print(f"  Invalid {label.lower()}. Please try again.")
            continue
        return value
    
#Features
def add_contact(contacts):
    print("\n--- Add Contact ------")
    name = normalize_name(prompt("Name"))

    if name in contacts:
        print(f"  '{name}' already exists. Use Edit to change it.")
        return

    phone = prompt("Phone", validator=validate_phone, hint="e.g. +256 700 123456")
    email = prompt("Email", validator=validate_email, hint="e.g leone@example.com")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"  Contact '{name}' added successfully.")

#Deleting contacts
def delete_contacts(contacts):
    print("\n--- Delete Contact ------")
    if not contacts:
        print(" No contacts found.")
        return

    name = normalize_name(prompt("Name to delete"))
    if name not in contacts:
        print(f" '{name}' not found.")
        return

    confirm = input(f"  Delete '{name}'? (y/n): ").strip().lower()
    if confirm == "y":
        del contacts[name]
        save_contacts(contacts)
        print(f"  '{name}' deleted.")
    else:
        print(" Cancelled.")        

#Searching for contacts
def search_contacts(contacts):
    print("\n --- Search Contacts ----")
    if not contacts:
        print("No contacts found.")
        return

    query = input(" Search (name, phone or email): ").strip().lower()
    if not query:
        print("Search cannot be empty")
        return

    results = {
        name: info for name, info in contacts.items()
        if query in name.lower()
        or query in info["phone"].lower()
        or query in info["email"].lower()
    }

    if not results:
        print(" No matches found.")
    else:
        print(f"\n Found {len(results)} result(s):")
        for name, info in results.items():
            print_contact(name, info)

#Editing details of a given contact
def edit_contact(contacts):
    print("\n--- Edit Contact -----")
    if not contacts:
        print(" No contacts found.")
        return

    name = normalize_name(prompt("Name to edit"))
    if name not in contacts:
        print(f"  '{name}' not found.")
        return

    print(f" Editing '{name}' - press Enter to keep current value.")
    info = contacts[name]

    new_name_raw = input(f" New Name [{name}]: ").strip()
    new_name = normalize_name(new_name_raw) if new_name_raw else name

    new_phone = input(f" New Phone [{info['phone']}]: ").strip()
    if new_phone and not validate_phone(new_phone):
        print(" Invalid phone format. Phone not updated.")
        new_phone = info["phone"]
    elif not new_phone:
        new_phone = info["phone"]

    new_email = input(f" New Email [{info['email']}]: ").strip()
    if new_email and not validate_email(new_email):
        print(" Invalid email format. Email not updated.")
        new_email = info["email"]
    elif not new_email:
        new_email = info["email"]

    #Handles renaming 
    if new_name != name:
        if new_name in contacts:
            print(f"  '{new_name}' already exists. Name not changed.")
            new_name = name
        else:
            del contacts[name]

    contacts[new_name] = {"phone": new_phone, "email": new_email}
    save_contacts(contacts)
    print("  Contact updated successfully.")

#Lists all saved contacts
def list_contacts(contacts):
    print("\n--- All Contacts ----")
    if not contacts:
        print(" No contacts added yet.")
        return
    
    sorted_names = sorted(contacts.keys())
    print(f" {len(sorted_names)} contact(s) found:")
    for i, name in enumerate(sorted_names, 1):
        print_contact(name, contacts[name], index=i)

#Menu

MENU = """
  ------------------------
 |     Contact Manager    |
 |------------------------|
 |1. List all contacts    |
 |2. Add contact          |
 |3. Edit contact         |
 |4.Delete contact        |
 |5.Search contacts       |
 | 0.Exit                 |
  ------------------------
"""        

ACTIONS = {
    "1": list_contacts,
    "2": add_contact,
    "3": edit_contact,
    "4": delete_contacts,
    "5": search_contacts,
}      

def main():
    contacts = load_contacts()

    while True:
        print(MENU)
        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("\n Thank you Bye!\n")
            break
        elif choice in ACTIONS:
            ACTIONS[choice](contacts)
        else:
            print("  Invalid choice. Please enter 0-5.")

if __name__ == "__main__":
    main()                