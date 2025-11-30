students=[("Анна",21,4.5),("Петр",22,4.2),("Мария",19,4.8),("Иван",20,4.1),("Ольга",23,4.6)]
print("Студенты старше 20 лет:")
for student in students:
    if student[1]>20:
        print(f"- {student[0]} ({student[1]}), средний балл: {student[2]}")
best=max(students,key=lambda x:x[2])
print(f"Лучший студент: {best[0]}, средний балл: {best[2]}")
sorted_students=sorted(students,key=lambda x:x[0])
print("Отсортированные студенты:")
for student in sorted_students:
    print(f"- {student[0]}")