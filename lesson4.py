# a = str(input("Введите слово: "))
# res = 0
# for c in a.upper():
#     if c in ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R') or c in ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'):
#         res += 1
#     elif c in ('D', 'G') or c in ('Д', 'К', 'Л', 'М', 'П', 'У'):
#         res += 2
#     elif c in ('B', 'C', 'M', 'P') or c in ('Б', 'Г', 'Ё', 'Ь', 'Я'):
#         res += 3
#     elif c in ('F', 'H', 'V', 'W', 'Y') or c in ('Й', 'Ы'):
#         res += 4
#     elif c in ('K') or c in ('Ж', 'З', 'Х', 'Ц', 'Ч'):
#         res += 5
#     elif c in ('J', 'X') or c in ('Ш', 'Э', 'Ю'):
#         res += 8
#     elif c in ('Q', 'Z') or c in ('Ф', 'Щ', 'Ъ'):
#         res += 10

# print(res)

s = 'a a a b c a a d c d d'.split()
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
        print(i, end=" ")
    else:
        print(f"{i}_{dic[i]}", end=" ")
        dic[i] += 1 

stroka = "a a a b c a a d c d d".split()
slov = {}

for i in stroka:
    if i not in slov:
        print(i, end=" ")
    else:
        print(f"{i}_{slov[i]}", end=" ")
        
    slov[i] = slov.get(i,0) + 1