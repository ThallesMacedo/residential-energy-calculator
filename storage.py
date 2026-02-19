import json

def save_data(appliances):
    with open("appliances.json", "w") as file:
        json.dump(appliances, file)

def load_data():
    try:
        with open("appliances.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []