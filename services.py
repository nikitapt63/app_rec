from gen import gen_customer_obj, gen_house_obj_list


def recommend_houses(customer, house_list):
    print(customer, house_list)
    filtered = list(filter(lambda house: house.price <= customer.account, house_list))
    filtered.sort(key=lambda house: house.square, reverse=True)
    return filtered


print(recommend_houses(customer=gen_customer_obj(), house_list=gen_house_obj_list(10)))

