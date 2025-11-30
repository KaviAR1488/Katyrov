text_lines = []
while True:
    line = input()
    if line == "": break
    text_lines.append(line)
full_text = " ".join(text_lines)
words = full_text.lower().split()
word_stats = {}
for word in words:
    clean_word = word.strip('.,!?;:')
    word_stats[clean_word] = word_stats.get(clean_word, 0) + 1
print(f"Статистика слов: {word_stats}")