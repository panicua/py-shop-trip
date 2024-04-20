import datetime
from math import sqrt

from app.car import Car
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

    def choose_the_cheapest_shop_visit(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> tuple:

        print(f"{self.name} has {self.money} dollars")
        best_price = best_shop = None

        for shop in shops:
            total_trip_price_shop = self.money_spent_on_products(shop)
            total_trip_price_shop += self.money_spent_on_fuel(shop, fuel_price)

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {total_trip_price_shop}")

            if (
                    not best_price
                    or total_trip_price_shop
                    < best_price
            ):
                best_price = total_trip_price_shop
                best_shop = shop
        return best_price, best_shop

    def ride_home(self, best_shop_visit_price: float) -> None:
        print(f"{self.name} rides home\n{self.name} now has "
              f"{self.money - best_shop_visit_price} dollars\n")

    def money_spent_on_products(self, shop: Shop) -> float:
        total_products_price = 0
        for money_customer_need, shop_item_price in (
                zip(self.product_cart.values(), shop.products.values())
        ):
            total_products_price += money_customer_need * shop_item_price
        return total_products_price

    def money_spent_on_fuel(self, shop: Shop, fuel_price: float) -> float:
        one_way_distance = sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        )
        money_fuel_spent = round(self.car.fuel_consumption
                                 * fuel_price / 100 * one_way_distance * 2, 2)
        return money_fuel_spent

    def calculate_if_enough_money(
            self,
            best_shop_visit_price: float,
            best_shop_instance: Shop
    ) -> bool:
        if self.money >= best_shop_visit_price:
            print(f"{self.name} rides to {best_shop_instance.name}\n")
            return True

        print(f"{self.name} doesn't have enough "
              f"money to make a purchase in any shop")
        return False

    def interaction_with_cashier(self, best_shop_instance: Shop) -> None:
        str_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {str_date}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              "You have bought:")

        paper_check, cart_price = self._checkout_for_products(
            shop=best_shop_instance
        )

        for products_amount_and_price in paper_check:
            print(products_amount_and_price)

        print(f"Total cost is {cart_price} dollars\nSee you again!\n")

    def _checkout_for_products(self, shop: Shop) -> tuple[list[str], float]:
        total_cart_price = 0
        full_paper_check = []

        for products_amount_customer_need, (product_name, product_price) in (
                zip(self.product_cart.values(), shop.products.items())
        ):
            full_product_price = products_amount_customer_need * product_price
            # tests fail without it, they want rounded if it can be rounded
            if full_product_price == int(full_product_price):
                full_product_price = int(full_product_price)
            total_cart_price += full_product_price

            paper_check = (f"{products_amount_customer_need} {product_name}s "
                           f"for {full_product_price} dollars")
            full_paper_check.append(paper_check)

        return full_paper_check, total_cart_price
