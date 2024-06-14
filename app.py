from gen import gen_customer_obj, gen_house_obj_list
from services import recommend_houses


def run():
    customer = gen_customer_obj()
    house_list = gen_house_obj_list(100)
    recs = recommend_houses(customer, house_list)
    return recs


run()
