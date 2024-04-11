import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def checkout_for_products(
            self,
            customer: "Customer"
    ) -> tuple[list[str], float]:

        total_cart_price = 0
        full_paper_check = []

        for (
                (_, products_amount_customer_need),
                (product_name, product_price)
        ) in zip(customer.product_cart.items(), self.products.items()):
            full_product_price = products_amount_customer_need * product_price
            if full_product_price == int(full_product_price):
                full_product_price = int(full_product_price)
            total_cart_price += full_product_price

            paper_check = (f"{products_amount_customer_need} {product_name}s "
                           f"for {full_product_price} dollars")
            full_paper_check.append(paper_check)

        return full_paper_check, total_cart_price


class Cashier:
    @staticmethod
    def interaction_with_cashier(
            customer: "Customer",
            best_shop_instance: Shop
    ) -> None:
        str_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {str_date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought:")

        paper_check, cart_price = Shop.checkout_for_products(
            best_shop_instance,
            customer)
        for product_number_and_price in paper_check:
            print(product_number_and_price)

        print(f"Total cost is {cart_price} dollars\nSee you again!\n")
