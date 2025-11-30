phone_book = {"Анна": "123", "Иван": "456", "Мария": "789"}
while True:
    choice = input("1-контакты 2-добавить 3-удалить 4-выйти: ")
    if choice == "1":
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    elif choice == "2":
        name = input("Имя: ")
        if name in phone_book:
            print("Контакт уже есть!")
        else:
            phone_book[name] = input("Телефон: ")
    elif choice == "3":
        name = input("Имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
        else:
            print("Контакт не найден!")
    elif choice == "4":
        exit()