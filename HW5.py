'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и
не больше заданного максимума).
На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, max_number.
'''
list_1 = [1, 2, 3, 4, -5, 11, 8, 4, 1, -6, -5, 8]
min_number = 0
max_number = 10
for i in range(0, len(list_1)):
    if (min_number <= list_1[i] <= max_number):
            print(i, end=" ")



'''
Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
'''
a1 = 7
d = 2
n = 5

res_p = []
def progress(a1, d, n):
    if n == 0:
        return ""
    return progress(a1, d, n - 1) + " " + str(a1 + (n-1) * d)
print(progress(a1, d, n))



# Входные данные
n = 9
a1 = 'osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen'
a2 = 'anton'
a3 = 'aoooooooooontooooo'
a4 = 'elelelelelelelelelel'
a5 = 'ntoneeee'
a6 = 'tonee'
a7 = '253235235a5323352n25235352t253523523235oo235523523523n'
a8 = 'antoooooooooooooooooooooooooooooooooooooooooooooooooooon'
a9 = 'unton'
# Сформируем список из входных данных:
names = []
names.append(a1)
names.append(a2)
names.append(a3)
names.append(a4)
names.append(a5)
names.append(a6)
names.append(a7)
names.append(a8)
names.append(a9)
def checkAnton(mas):
    # Поиск первой буквы: a
    for a in range(0,len(mas)):
        if mas[a] == 'a':
            # Поиск второй буквы: n
            for n in range(a+1, len(mas)):
                if mas[n] == 'n':
                    # Поиск 3 буквы: t
                    for t in range(n+1, len(mas)):
                        if mas[t] == 't':
                            # Поиск 4 буквы: o
                            for o in range(t+1, len(mas)):
                                if mas[o] == 'o':
                                    # Поиск 5 буквы: n
                                    for n2 in range(o+1, len(mas)):
                                        if mas[n2] == 'n':
                                            return True
    return False
for j in range(len(names)):
    if checkAnton(names[j]) == True:
        print(j+1, end =' ')