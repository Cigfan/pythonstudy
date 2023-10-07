import math
import random

'''
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует 
выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
Формат входных данных
На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
Sample Input 1:
ОРРОРОРООРРРО
Sample Output 1:
3
'''
mon = list(input("Введите последовательность: "))
print(mon, type(mon))
count = 0
temp = 0
res = 0
while count < len(mon):
    if mon[count] == "р":
        temp = temp + 1
    else:
        if temp > res:
            res = temp
            temp = 0
        else:
            temp = 0
    count = count + 1
print(res)


'''
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
'''

a = int(input("Введите число: "))
coins = [random.randint(0,1) for _ in range(a)]
i = 0
heads = 0
tails = 0
while i < len(coins):
    if coins[i] == 1:
        heads = heads + 1
    else:
        tails = tails + 1
    i = i + 1
if heads > tails:
    print(f"Нужно перевернуть {tails} монет(ы).")
else:
    print(f"Нужно перевернуть {heads} монет(ы).")

'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
discr = s ** 2 - 4 * -1 * -p
if discr > 0:
    x1 = (-s + math.sqrt(discr)) / (2 * -1)
    x2 = (-s - math.sqrt(discr)) / (2 * -1)
    print(f"Первое число = {int(x1)}, Второе число = {int(x2)}")
elif discr == 0:
    x = -s / (2 * -1)
    print(f"Оба числа = {int(x)}")

'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числаN.
'''

check = int(input("Введите число: "))
d = 1
while(d < check):
    print(d)
    d*=2


'''
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
'''

days = int(input("Введите количество дней: "))
weather = [random.randint(-50, 50) for _ in range(days)]
countd = 0
tempd = 0
resd = 0
print(weather)
while countd < len(weather):
    if weather[countd] > 0:
        tempd = tempd + 1
    else:
        if tempd > resd:
            resd = tempd
            tempd = 0
        else:
            tempd = 0
    countd = countd + 1
print(resd)