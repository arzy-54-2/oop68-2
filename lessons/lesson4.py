# | Метод         | Что делает                |
# | ------------- | ------------------------- |
# | `__init__`    | конструктор               |
# | `__str__`     | вывод через `print()`     |
# | `__repr__`    | отображение объекта       |
# | `__len__`     | `len(obj)`                |
# | `__getitem__` | `obj[key]`                |
# | `__call__`    | вызов объекта как функции |
# | `__eq__`      | `==`                      |
# | `__lt__`      | `<`                       |
# | `__gt__`      | `>`                       |
from lessons.lesson3 import ardager


# | Оператор | Магический метод | Пример   |
# | -------- | ---------------- | -------- |
# | `+`      | `__add__`        | `a + b`  |
# | `-`      | `__sub__`        | `a - b`  |
# | `*`      | `__mul__`        | `a * b`  |
# | `/`      | `__truediv__`    | `a / b`  |
# | `//`     | `__floordiv__`   | `a // b` |
# | `%`      | `__mod__`        | `a % b`  |

class Test:

    def __init__(self, value):
        self.value = value
        self.view_count = 0

    def __str__(self):
        return str(self.value)

    def __add__(self, other):

        # if type(self) == type(other)
       return self.value + other.value

    def __lt__(self, other):
        return self.value < other.value

    def __call__(self):
        self.view_count +=1
        print('Меня вызвали')

test_obj = Test(123)
test_obj_2 = Test(12432)
py_int = 123
py_int_2 = 123

# print(test_obj_2.view_count)
# test_obj_2()
# test_obj_2()
# test_obj_2()
# print(test_obj_2.view_count)
# sum_int = test_obj == test_obj_2
# print(sum_int)


class Money:
    def __init__(self, currency, sum):
        self.currency = currency
        self.sum = sum

    def __convert_to_sum(self, money):
        pass

    # def __add__(self, other):
    #     if self.currency != other.currency:
    #


som = Money('SOM', 100)
usd = Money('USD', 100)
# total_balance = som + usd



class Add:

    def __init__(self, value):
        self.value = value


    def get_value(self):
        return self.value

    @staticmethod
    def add_int( a, b):
        return a + b


# test_1 = Add(123)
# print(Add.add_int(123, 123))

class BankAccount:
    # Артибута класса
    bank_name = "Kompanion"

    def __init__(self, name, balance, bonus, total_balance):
        # Артибуты экземпляра класса
        self.name = name
        self.first_name = name
        self.last_name = name
        self._balance = balance
        self.__bonus = bonus
    def get_name(self):
        return self.name.

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

    @property
    def balance(self):
        return self._balance

    @property
    def total_balance(self):
        return self._balance + self.__bonus

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @balance.setter
    def balance(self, value):
        self._balance = value



ardager_1 = BankAccount('Name', 100, 50)
ardager_2 = BankAccount(ardager_1, 100, 50)
print(ardager_1.name)
ardager_1.name = "Ардагер"
print(ardager_1.name)
print(ardager_1._balance)
ardager_1.balance = 9999
print(ardager_1._balance)

column = (
    'full_name' , '_balance', 'bonus', 'total_balance'
)





















