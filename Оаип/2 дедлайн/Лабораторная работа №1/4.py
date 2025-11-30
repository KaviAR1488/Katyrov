from random import randint
random_num = randint(1, 100)
while True:
    guess = int(input())
    if guess == random_num:
        print("Угадал!")
        break
    print("Меньше" if guess > random_num else "Больше")