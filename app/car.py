import json
from dataclasses import dataclass


@dataclass
class Car:
    brand: str = None
    fuel_consumption: float = None


def load_fuel_price_from_json(filepath: str) -> float:
    with open(filepath, "r") as file:
        data = json.load(file)
        return data.get("FUEL_PRICE")


FUEL_PRICE = load_fuel_price_from_json("app/config.json")
