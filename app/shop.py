from math import sqrt

from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products


def shop_visit_price_calculation(customer: Customer,
                                 shop: Shop,
                                 fuel_price: float) -> dict:
    total_price = 0
    for (_, value_need_customer), (_, shop_item_price) in zip(
            customer.product_cart.items(), shop.products.items()
    ):
        total_price += value_need_customer * shop_item_price

    one_way_distance = sqrt(
        (customer.location[0] - shop.location[0]) ** 2
        + (customer.location[1] - shop.location[1]) ** 2
    )
    total_price += round(customer.car.fuel_consumption
                         * fuel_price / 100 * one_way_distance * 2, 2)

    return {"total_price": total_price,
            "shop": shop}


def checkout_for_products(customer: Customer,
                          shop_instance: Shop) -> tuple[list[str], float]:
    total_cart_price = 0
    full_paper_check = []

    for ((_, products_amount_customer_need),
         (product_name, product_price)) in zip(
        customer.product_cart.items(),
        shop_instance.products.items()
    ):
        full_product_price = products_amount_customer_need * product_price
        if full_product_price == int(full_product_price):
            full_product_price = int(full_product_price)
        total_cart_price += full_product_price

        paper_check = (f"{products_amount_customer_need} {product_name}s "
                       f"for {full_product_price} dollars")
        full_paper_check.append(paper_check)

    return full_paper_check, total_cart_price
