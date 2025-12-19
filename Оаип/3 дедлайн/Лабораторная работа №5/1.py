class Student:
    def __init__(self,name,average_score):
        self.name=name
        self.average_score=average_score
    def is_excellent(self):
        return self.average_score==5