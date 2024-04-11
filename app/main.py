from app.customer import Customer
from app.load_jsons import load_complete_json
from app.shop import Shop


def shop_trip() -> None:
    data = load_complete_json("app/config.json")
    customers = [Customer(**customer_) for customer_ in data.get("customers")]
    shops = [Shop(**shop) for shop in data.get("shops")]
    fuel_price = data.get("FUEL_PRICE")

    for customer in customers:
        Customer.choose_the_cheapest_shop_visit(customer, shops, fuel_price)


if "__main__" == __name__:
    shop_trip()
