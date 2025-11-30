import random
numbers = [random.randint(1, 100) for _ in range(10)]
even_numbers = [num for num in numbers if num % 2 == 0]
numbers_above_50 = [num for num in numbers if num > 50]
print(f"Исходный список: {numbers}")
print(f"Четные числа: {even_numbers}")
print(f"Числа больше 50: {numbers_above_50}")