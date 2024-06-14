class House:
    def __init__(self, price, square, room_count):
        self.price = price
        self.square = square
        self.room_count = room_count

    def __str__(self):
        return f"Price: {self.price}$, Square: {self.square}m2"

    def __repr__(self):
        return f"{self.price}$ - {self.square}m2"


class Customer:
    def __init__(self, name, surname, account):
        self.name = name
        self.surname = surname
        self.account = account

    def get_full_name(self):
        full_name = f"{self.name} {self.surname}"
        return full_name

    def __str__(self):
        return f"Full Name: {self.get_full_name()} Account: {self.account}$"

    def __repr__(self):
        return f"{self.get_full_name()} - {self.account}$"
