'''
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются 
только +1 и -1. Также нельзя использовать циклы. Функция не должна ничего выводить, только возвращать значение.
'''

x = str(input("Введите числа через пробел: ")).split()
a = int(x[0])
b = int(x[1])
def sum(a, b):
    if b == 0:
        return a
    else:
        return 1 + sum(a, b - 1)
print(sum(a, b))

'''
Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
Функция не должна ничего выводить, только возвращать значение.
'''
z = str(input("Введите число и степень через пробел: ")).split()
c = int(z[0])
d = int(z[1])
def pow(c, d):
    if d <= 1:
        return c
    return c*pow(c, d-1)
print(pow(c, d))