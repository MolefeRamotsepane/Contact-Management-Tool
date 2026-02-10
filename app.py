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