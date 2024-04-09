import json


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def load_shops_from_json(filepath: str) -> list[Shop]:
    with open(filepath, "r") as file:
        data = json.load(file)
        shops_data = data.get("shops")
        return [Shop(**shop_) for shop_ in shops_data]


shops_ = load_shops_from_json("app/config.json")
