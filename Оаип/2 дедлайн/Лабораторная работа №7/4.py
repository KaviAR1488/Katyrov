call_counter=0
def increment_counter():
    """Увеличивает глобальный счетчик вызовов."""
    global call_counter
    call_counter+=1