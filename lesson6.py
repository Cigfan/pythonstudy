import random
'''Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3'''

x = int(input("Введите размеры массива через пробел: "))
def rotate(x):
    if x == 0:
        return ""
    num = input("введите число: ")
    return num + (rotate(x-1)) 
print(rotate(x))

s = []

for i in range(1, 5000):
    sum1 = 0
    for j in range(1, i//2+1):
        if i%j == 0:
            sum1 += j
    s.append([i, sum1])
# print(s)
for p in range(len(s)):
    for b in range(p, len(s)):
        if p != b and s[b][0] == s[p][1] and s[b][1] == s[p][0]:
            print(s[b])