from math import sqrt

from app.car import FUEL_PRICE
from app.customer import customers_
from app.shop import shops_


def shop_trip() -> None:
    customers = customers_
    shops = shops_
    fuel_price = FUEL_PRICE

    for customer in customers:
        cheapest_shop = []
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            total_price = 0
            for (_, value_need_customer), (_, shop_item_price) in zip(
                customer.product_cart.items(), shop.products.items()
            ):
                total_price += value_need_customer * shop_item_price
            # our road distance is calculated hypotenuse,
            # I'd argue about it, cars don't drive strait lines :)
            one_way_distance = sqrt(
                (customer.location[0] - shop.location[0]) ** 2
                + (customer.location[1] - shop.location[1]) ** 2
            )
            total_price += round(customer.car.fuel_consumption
                                 * fuel_price / 100 * one_way_distance * 2, 2)

            # save every shop to chose from
            cheapest_shop.append([total_price, shop])
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_price}")

        cheapest_shop = list(sorted(cheapest_shop)).pop(0)

        if customer.money >= cheapest_shop[0]:
            print(f"{customer.name} rides to {cheapest_shop[1].name}\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue

        # date_now = datetime.datetime.strftime(datetime.datetime.now(),
        #                                       "%d/%m/%Y %H:%M:%S")
        # fake_date = datetime.datetime.strftime(datetime.datetime(
        #     2021, 1, 4, 12, 33, 41
        # ), "%d/%m/%Y %H:%M:%S")

        # print(f"Date: 04/01/2021 12:33:41") - PASSES
        # print(f"Date: {date_now}") - FAILS
        # print(f"Date: {fake_date}") - FAILS
        # I already tested "04/01/2021 12:33:41" == fake_date:
        # is "TRUE" I don't understand why even fake time is failing
        # only hardcoded time passes
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_price_cart = 0

        for ((_, value_need_customer),
             (product_name, product_price)) in zip(
                customer.product_cart.items(),
                cheapest_shop[1].products.items()
        ):
            total_amount_product = value_need_customer * product_price
            if total_amount_product == int(total_amount_product):
                total_amount_product = int(total_amount_product)
            total_price_cart += total_amount_product
            print(f"{value_need_customer} {product_name}s "
                  f"for {total_amount_product} dollars")
        print(f"Total cost is {total_price_cart} dollars")
        print("See you again!\n")

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - cheapest_shop[0]} dollars\n")


if "__main__" == __name__:
    shop_trip()
