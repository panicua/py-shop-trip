import json

from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)


def load_customers_from_json(filepath: str) -> list[Customer]:
    with open(filepath, "r") as file:
        data = json.load(file)
        customers_data = data.get("customers")
        return [Customer(**customer_) for customer_ in customers_data]


customers_ = load_customers_from_json("app/config.json")
