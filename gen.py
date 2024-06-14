from models import House, Customer
from random import randint, choice
from data import CRED_DATA


def gen_customer_obj():
    """Generate Customer object."""
    customer = Customer(
        name=choice(CRED_DATA["names"]),
        surname=choice(CRED_DATA["surnames"]),
        account=randint(20_000, 200_000))
    return customer


def gen_house_obj_list(count: int):
    """Generate House object list with random attrs."""
    house_list = []
    for _ in range(count):
        house = House(
            price=randint(20_000, 200_000),
            square=randint(30, 200),
            room_count=randint(1, 8))
        house_list.append(house)
    return house_list
