"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.

"""


def degree_counter(number=2, limit=1000, degree=0):
    flag = True
    pow = 0
    while flag:
        if pow > limit:
            flag = False
        if degree % 2 == 0:
            pow = number ** degree
            print(pow)
        degree += 1


degree_counter()
