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

def save_contacts(contacts):
    """Save contacts to the contacts.json file."""
    # Open the contacts.json file in write(w) mode and save the contacts list as JSON data
    with open(FILE_NAME, "w") as file:
        # json.dump() will convert the python object (contacts) into a JSON formatted string and write it to the file
        json.dump(contacts, file, indent=4) # indent=4 is used for pretty-printing(indentation) the JSON data