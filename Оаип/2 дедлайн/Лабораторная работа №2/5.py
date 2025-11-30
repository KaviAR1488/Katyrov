count = int(input("Сколько чисел вы хотите ввести? "))
numbers = []
for i in range(count):
    num = int(input(f"Введите число {i + 1}: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / count
above_average = sum(1 for num in numbers if num > average)

print("Результаты:")
print(f"Максимальное: {maximum}")
print(f"Минимальное: {minimum}")
print(f"Среднее: {average}")
print(f"Чисел больше среднего: {above_average}")