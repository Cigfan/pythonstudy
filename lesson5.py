'''факториал'''

# x = int(input("Введите цифру рекурсии: "))
# def factorial(x):
#     if x <= 1:
#         return x
#     return x * factorial(x-1)
# print(factorial(x))

'''фибоначи'''

# y = int(input("Введите  "))
# def fib(y):
#     if y <= 1:
#         return 1
#     return fib(y - 1) + fib(y - 2)
# print(fib(y))

'''Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes'''

z = int(input("Введите число: "))
def nat(z, x = 2):
    if z == 2 or x * x > z:
        return True
    elif z % x == 0:
        return False 
    return nat(z, x + 1)

print(nat(z))