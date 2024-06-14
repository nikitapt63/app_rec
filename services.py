def recommend_houses(customer, house_list):
    filtered = list(filter(lambda house: house.price <= customer.account, house_list))
    filtered.sort(key=lambda house: house.square, reverse=True)
    return filtered
