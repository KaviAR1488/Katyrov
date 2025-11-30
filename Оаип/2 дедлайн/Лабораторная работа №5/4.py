text=input("Введите текст: ").lower()
words=set(text.split())
long_words={word for word in words if len(word)>5}
has_keywords="python" in words or "programming" in words
print(f"Уникальные слова: {len(words)}")
print(f"Длинные слова: {long_words}")
print(f"Найдены ключевые слова: {has_keywords}")