def calc_avg(numbers:list)->float:
    """Вычисляет среднее арифметическое списка чисел.
    Args:
        numbers:Список чисел
    Returns:
        Среднее значение чисел"""
    if not numbers:
        return 0.0
    return sum(numbers)/len(numbers)

def fmt_fio(parts:list,capitalize:bool=True)->str:
    """Форматирует ФИО из списка частей.
    Args:
        parts:Список частей ФИО
        capitalize:Приводить к заглавным буквам
    Returns:
        Отформатированная строка ФИО"""
    fio=" ".join(parts)
    if capitalize:
        return fio.title()
    return fio

def filter_scores(data_dict:dict,min_value:int)->dict:
    """Фильтрует словарь по минимальному значению.
    Args:
        data_dict:Словарь для фильтрации
        min_value:Минимальное значение
    Returns:
        Отфильтрованный словарь"""
    result={}
    for key,value in data_dict.items():
        if value>=min_value:
            result[key]=value
    return result

print(calc_avg([10,20,30,40]))
print(fmt_fio(["петров","иван","сергеевич"]))
print(fmt_fio(["сидорова","анна","валерьевна"],capitalize=False))
scores={"math":95,"history":78,"english":88,"art":92}
print(filter_scores(scores,90))