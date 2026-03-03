import json

FILE_NAME = "bugs.json"

def load_bugs():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_bugs(bugs):
    with open(FILE_NAME, "w") as file:
        json.dump(bugs, file, indent=4)