s = input().lower().replace(" ", "")
left, right = 0, len(s) - 1
is_palindrome = True
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print("Да, это палиндром" if is_palindrome else "Нет, это не палиндром")