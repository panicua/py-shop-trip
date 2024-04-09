from dataclasses import dataclass
import json


@dataclass
class Car:
    brand: str = None
    fuel_consumption: float = None


def load_fuel_price_from_json(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
        return data.get("FUEL_PRICE")


FUEL_PRICE = load_fuel_price_from_json("app/config.json")


# if "__main__" == __name__:
#     load_fuel_price_from_json("config.json")