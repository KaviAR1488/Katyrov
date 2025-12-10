def safe_exec(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")
            return 0
    return wrapper