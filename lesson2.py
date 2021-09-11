# 1
class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"Название товара: {self.name}, цена товара: {self.price} руб."


a = ItemDiscountReport('Телефон', 20000)
print(a.get_parent_data())

# 2
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"Название товара: {self.__name}, цена товара: {self.__price} руб."


a = ItemDiscountReport('Телефон', 20000)
print(a.get_parent_data())

#3
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"Название товара: {self.name}, цена товара: {self.price} руб."


a = ItemDiscountReport('Телефон', 20000)
print(a.get_parent_data())

# 4
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f"Название товара: {self.name}, цена товара: {self.price} руб."


a = ItemDiscountReport('Телефон', 20000)
a.set_price(50000)
print(a.get_parent_data())

# 5
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount=0):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return f"Название товара: {self.name}, цена без скидок {self.price} руб., " \
               f"цена со скидкой {self.discount}%: {self.price - self.price * self.discount/100} руб."


a = ItemDiscountReport('Телефон', 20000, 25)
print(a)

# 6
class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport1(ItemDiscount):
    def get_info(self):
        return self.name


class ItemDiscountReport2(ItemDiscount):
    def get_info(self):
        return self.price


a = ItemDiscountReport1('Телефон', 20000)
print(a.get_info())

b = ItemDiscountReport2('Компьютер', 100000)
print(b.get_info())

for item in (a, b):
    print(item.get_info())

def function(obj):
    return obj.get_info()

print(function(a))
print(function(b))
