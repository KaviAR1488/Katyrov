s = input()
vowels = "аеёиоуыэюяaeiou"
result = ""
i = 0
while i < len(s):
    if s[i].lower() not in vowels:
        result += s[i]
    i += 1
print(result)