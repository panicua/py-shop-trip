from collections import defaultdict
from math import sqrt

from app.car import Car
from app.shop import Cashier
from app.shop import Shop


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

    def choose_the_cheapest_shop_visit(self,
                                       shops: list[Shop],
                                       fuel_price: float) -> None:
        best_price_and_shop = defaultdict()
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            total_trip_price_shop = (
                Customer._shop_visit_price_calculation(self, shop, fuel_price)
            )
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {total_trip_price_shop['total_price']}")

            if (
                    not best_price_and_shop
                    or total_trip_price_shop["total_price"]
                    < best_price_and_shop["total_price"]
            ):
                best_price_and_shop = total_trip_price_shop

        best_shop_visit_price: float = best_price_and_shop["total_price"]
        best_shop_instance: Shop = best_price_and_shop["shop"]

        if self.money >= best_shop_visit_price:
            print(f"{self.name} rides to {best_shop_instance.name}\n")

            Cashier.interaction_with_cashier(self, best_shop_instance)
            self.ride_home(best_shop_visit_price)
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")

    def _shop_visit_price_calculation(self,
                                      shop: Shop,
                                      fuel_price: float) -> dict:
        total_price = 0
        for (_, value_need_customer), (_, shop_item_price) in zip(
                self.product_cart.items(), shop.products.items()
        ):
            total_price += value_need_customer * shop_item_price

        one_way_distance = sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        )
        total_price += round(self.car.fuel_consumption
                             * fuel_price / 100 * one_way_distance * 2, 2)

        return {"total_price": total_price,
                "shop": shop}

    def ride_home(self, best_shop_visit_price: float) -> None:
        print(f"{self.name} rides home\n{self.name} now has "
              f"{self.money - best_shop_visit_price} dollars\n")
