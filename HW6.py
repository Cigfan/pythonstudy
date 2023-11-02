def honey_boy(row):
    
    letters = 'уеыаоэяию'
    str_split = list(map(lambda x: x.split("-"), row.split(" ")))
    result = []
    for phrase in str_split:
        count = 0
        for let in list("".join(phrase)):
            if let in letters:
                count+=1
        result.append(count)
    
    
    if len(result) == 1:
        print("Количество фраз должно быть больше одной!")
    else:  
        if sum(result) / len(result) == result[0]:
            print("Парам пам-пам")
        else:
            print("Пам парам")
    
honey_boy(stroka)