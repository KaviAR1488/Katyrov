text = input()
word = input()
count = text.count(word)
print(f"{count} times" if count > 0 else "Not found")