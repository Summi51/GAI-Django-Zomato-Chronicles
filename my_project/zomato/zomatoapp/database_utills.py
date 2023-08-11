import json

DB_FILE = "db.json"

def read_data():
    with open(DB_FILE, "r") as file:
        data = json.load(file)
        return data.get("menu", []), data.get("orders", [])


def write_data(menu_data, orders_data):
    data = {"menu": menu_data, "orders": orders_data}
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

