import json


def load_complete_json(filepath: str) -> dict:
    with open(filepath, "r") as file:
        data = json.load(file)
        return data
