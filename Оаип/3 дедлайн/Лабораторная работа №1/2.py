def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper