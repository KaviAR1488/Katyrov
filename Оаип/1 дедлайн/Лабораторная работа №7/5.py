a, op, b = input().split()
a, b = float(a), float(b)
print(a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a / b if b != 0 else "Error: division by zero")