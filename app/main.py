from collections import defaultdict

from app.customer import Customer
from app.load_jsons import load_complete_json
from app.shop import Shop, shop_visit_price_calculation, checkout_for_products


def shop_trip() -> None:
    data = load_complete_json("app/config.json")
    customers = [Customer(**customer_) for customer_ in data.get("customers")]
    shops = [Shop(**shop) for shop in data.get("shops")]
    fuel_price = data.get("FUEL_PRICE")

    for customer in customers:
        best_price_and_shop = defaultdict()
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            total_price_and_shop = shop_visit_price_calculation(customer,
                                                                shop,
                                                                fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_price_and_shop['total_price']}")

            if (not best_price_and_shop or total_price_and_shop["total_price"]
                    < best_price_and_shop["total_price"]):
                best_price_and_shop = total_price_and_shop

        best_shop_visit_price: float = best_price_and_shop["total_price"]
        best_shop_instance: Shop = best_price_and_shop["shop"]

        if customer.money >= best_shop_visit_price:
            print(f"{customer.name} rides to {best_shop_instance.name}\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue

        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        paper_check, cart_price = checkout_for_products(customer,
                                                        best_shop_instance)
        for product_number_and_price in paper_check:
            print(product_number_and_price)

        print(f"Total cost is {cart_price} dollars")
        print("See you again!\n")

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - best_shop_visit_price} dollars\n")


if "__main__" == __name__:
    shop_trip()
