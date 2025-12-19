class LoggableMixin:
    def log(self,message):
        print(f"[INFO] {self.__class__.__name__}: {message}")
class Employee(LoggableMixin):
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value<0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._salary=value