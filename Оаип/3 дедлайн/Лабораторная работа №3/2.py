def sum_digits(number):
    if number==0:
        return 0
    return number%10+sum_digits(number//10)