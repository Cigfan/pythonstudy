import os, re


def phone_format(n):
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Фамилия        Имя          Номер телефона")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "фамилия": lastName,
                "имя": name,
                "телефон": phone_format(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)


def showContacts(fileName):
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- нажмите для продолжения Enter ---")


def addContact(fileName):
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию контакта: ") + ","
        res += input("Введите имя контакта: ") + ","
        res += input("Введите номер телефона контакта: ")

        file.write(res + "\n")

    input("\nКонтакт был успешно добавлен!\n--- нажмите для продолжения Enter ---")


def findContact(fileName):
    os.system("cls")
    target = input("Введите данные контакта для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"С этими данными нет контакта '{target}'.")

    input("--- нажмите для продолжения Enter ---")


def changeContact(fileName):
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для изменения или 0 для возврата в главное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый номер телефона: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен!")
                input("\n--- нажмите для продолжения Enter ---")
        else:
            return


def deleteContact(fileName):
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для удаления или 0 для возврата в главное меню: ")
        )
        if numberContact != 0:
            print(f"Удаление записи: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- нажмите для продолжения Enter ---")


def drawInterface():
    print("#####   ТЕЛЕФОННАЯ КНИГА   #####")
    print("=" * 26)
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавить контакты")
    print(" [3] -- Поиск контакта")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")
    print("=" * 26)


def main(file_name):
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите число от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Работа программы завершена")
            return


path = "phonebook.txt"

main(path)