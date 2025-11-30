text=input("Введите текст: ")
import string
words=text.lower().split()
clean_words=[word.strip(string.punctuation) for word in words]
longest_word=max(clean_words,key=len)
shortest_word=min(clean_words,key=len)
avg_length=sum(len(word) for word in clean_words)/len(clean_words)
word_count={}
for word in clean_words:
    word_count[word]=word_count.get(word,0)+1
top_5=sorted(word_count.items(),key=lambda x:x[1],reverse=True)[:5]
print(f"Самое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")
print(f"Средняя длина: {avg_length:.1f}")
print(f"Топ-5 слов: {top_5}")