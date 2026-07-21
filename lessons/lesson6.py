# Декоратор
def simple_decorator(func):
    def wrapper():
        print('До выполнения!!!')
        func()
        print('после выполнения!!')
    return wrapper

# @simple_decorator
# def hello():
#     print('Hello')

# hello()



# @greeting
# def say_hello(name):
#     print(f"Как дела {name}?")


# say_hello('Ardager')
def greeting(func):
    def wrapper(name):
        print(f'Привет {name}')
        func(name)
    return wrapper

def repeat_decorator(value):
    def decorator(func):
        def wrapper(name):
            for i in range(value):
                func(name)
        return wrapper
    return decorator


@greeting
@repeat_decorator(5)
def say_hello(name):
    print(f"Как дела {name}?")

# say_hello("Ardager")


def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print("New action!!")
    return NewClass

# @class_decorator
class OldClass:
    def action(self):
        print("Old action!!")

test_obj = OldClass()

test_obj.action()
print(type(test_obj))