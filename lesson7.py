# x = input("Введите что-то: ")
# def prnt(x):
#    return x
# print(prnt(5))

# prnt1 = lambda x: x
# print(prnt1(7))

# print((lambda x: x)(9))

# numbers = "12345"
# numbers = list(numbers)
# print(numbers)

# numbers = list(map(int, numbers))
# print(numbers)

# numbers = list(map(lambda x: x * 2, numbers))
# print(numbers)

# numbers1 = list(filter(lambda x: x % 4 == 0, numbers))
# print(numbers1)

# numbers2 = list(filter(lambda x: x % 4, numbers))
# print(numbers2)

'''У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
Пример ввода и вывода данных представлены на следующем слайде'''



'''Задача No47. Решение в группах
Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values)) if values == transformed_values:
print(‘ok’) else:
print(‘fail’)
Вывод:
ok
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
print(‘same’) else:
print(‘different’)'''

# values = [0, 2, 10, 6] 
# def same_by(characteristic, objects):
#     if objects == list(filter(characteristic, objects)):
#         return True
#     return False
# if same_by(lambda x: x % 2 == 0, values):
#     print('same') 
# else:
#     print('different')

values = [0, 2, 10, 6] 
def same_by(characteristic, objects):
    return list(filter(characteristic, objects)) == 0
if same_by(lambda x: x % 2 == 0, values):
    print('same') 
else:
    print('different')