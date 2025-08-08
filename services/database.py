import json
import os

FILE_PATH = "data/users.json"

def load_users():
    if not os.path.exists(FILE_PATH):
        return {"users": {}}
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def save_users(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def update_user(chat_id, key, value):
    data = load_users()
    chat_id = str(chat_id)
    if chat_id not in data["users"]:
        data["users"][chat_id] = {
            "name": "",
            "gender": "",
            "location": {"longatute": 0.0, "latetute": 0.0},
            "number": ""
        }
    if key == "location":
        data["users"][chat_id]["location"] = value
    else:
        data["users"][chat_id][key] = value
    save_users(data)
