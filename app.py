import json # for handling JSON data
import os # for handling file paths and directories

FILE_NAME = "contacts.json" # name of the file to store contacts

def load_contacts():
    """Load contacts from the contacts.json file."""
    # Check if the contacts.json file exists
    if os.path.exists(FILE_NAME):
        # If it does, open it in read(r) mode and load the JSON data
        with open(FILE_NAME, "r") as file:
            # json.load() will parse(read) the JSON data into a Python object
            # which is then returned by this function
            return json.load(file)
    return [] # return an empty list if the file does not exist

def save_contacts(contacts): # contacts is a list of contact dictionaries that we want to save to the file
    """Save contacts to the contacts.json file."""
    # Open the contacts.json file in write(w) mode and save the contacts list as JSON data
    with open(FILE_NAME, "w") as file:
        # json.dump() will convert the python object (contacts) into a JSON formatted string and write it to the file
        json.dump(contacts, file, indent=4) # indent=4 is used for pretty-printing(indentation) the JSON data

def add_contact(contacts):
    name = input("Enter name: ") # prompt the user to enter a name
    phone = input("Enter phone number: ") # prompt the user to enter a phone number
    email = input("Enter email: ") # prompt the user to enter an email address

    contact = {
        "name": name, # store the entered name in the contact dictionary
        "phone": phone, # store the entered phone number in the contact dictionary
        "email": email # store the entered email address in the contact dictionary
    }

    contacts.append(contact) # add the new contact to the contacts list
    save_contacts(contacts) # save the updated contacts list to the file

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.") # if the contacts list is empty, print a message indicating that no contacts are found
        return
    
    for contact in contacts: # iterate(loop) through each contact in the contacts list
        print(f"Name: {contact["name"]}") # print the name of the contact
        print(f"Phone: {contact["phone"]}") # print the phone number of the contact
        print(f"Email: {contact["email"]}") # print the email address of the

def search_contacts(contacts):
    search_name = input("Enter name to seacrh: ") # prompt the user to enter a name to search for
    for contact in contacts: # iterate(loop) through each contact in the contacts list
        if contact["name"].lower() == search_name.lower(): # check if the name of the contact is equal to the entered name
            print("Conact found:") # if a contact with the entered name is found, print a message indicating that the contact is found
            print(contact)
            return
    print("Contact not found.") # if no contact with the entered name is found, print a message indicating that the contact is not found

def delete_contact(contacts):
    name = input("Enter name to delete: ") # prompt the user to enter a name to delete
    for contact in contacts: # iterate(loop) through each contact in the contacts list
        if contact["name"].lower() == name.lower(): # check if the name of the contact is equal to the entered name
            contacts.remove(contact) # if a contact with the entered name is found, remove it from the contacts list
            save_contacts(contacts) # save the updated contacts list to the file
            print("Contact deleted.") # print a message indicating that the contact is deleted
            return
    print("Contact not found.") # if no contact with the entered name is found, print a message indicating that the contact is not found

def main(): # main function that runs the program
    contacts = load_contacts() # load contacts from the file