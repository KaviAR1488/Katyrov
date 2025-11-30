tasks = []
while True:
    print("1 - Показать задачи")
    print("2 - Добавить задачу") 
    print("3 - Удалить задачу")
    print("4 - Выйти")
    choice = input("Выберите действие: ")
    if choice == "1":
        if tasks:
            print("Ваши задачи:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Задач нет!")
    elif choice == "2":
        task = input("Введите задачу: ")
        tasks.append(task)
    elif choice == "3":
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Какую задачу выполнили? ")) - 1
            removed = tasks.pop(num)
            print(f'Задача "{removed}" удалена!')
        else:
            print("Задач нет!")
    elif choice == "4":
        break