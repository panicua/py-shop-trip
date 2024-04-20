from app.customer import Customer
from app.load_jsons import load_complete_json
from app.shop import Shop


def shop_trip() -> None:
    data = load_complete_json("app/config.json")
    shops = [Shop(**shop) for shop in data.get("shops")]
    fuel_price = data.get("FUEL_PRICE")

    for customer_data in data.get("customers"):
        customer = Customer(**customer_data)
        best_price, best_shop = customer.choose_the_cheapest_shop_visit(
            shops=shops, fuel_price=fuel_price
        )
        is_enough_money = customer.calculate_if_enough_money(
            best_shop_visit_price=best_price, best_shop_instance=best_shop
        )
        if not is_enough_money:
            continue

        customer.interaction_with_cashier(best_shop_instance=best_shop)
        customer.ride_home(best_shop_visit_price=best_price)
