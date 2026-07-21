import sqlite3

# import module1
# from module1 import *
#
#
# ardager = Hero("Ardager", 100, 100)
# ardager2 = Hero2("Ardager", 100, 100)
# ardager3 = Hero3("Ardager", 100, 100)
#
# print(test)
# print(random.randint(10, 100))


from my_package import Hero, test, MageHero, add
from lessons.lesson6 import repeat_decorator


ardager = Hero("Ardager", 100, 100)

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(test)
print(add(12, 13))
print(Style.RESET_ALL)
print('back to normal now')