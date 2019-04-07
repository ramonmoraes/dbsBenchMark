import json


def insert_data():
    data = {}
    print("loading data")
    with open("data/full_dataset.json", "r") as f:
        return json.load(f)
