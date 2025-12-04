s=input().replace(',',' ').replace('.',' ').split()
uppercount=0
vowelcount=0
longest=''
for word in s:
    if word[0].isupper():uppercount+=1
    if word[-1] in 'aeiouаеёиоуыэюяAEIOUAEЁИОУЫЭЮЯ':vowelcount+=1
    if len(word)>len(longest):longest=word
print(uppercount)
print(vowelcount)
print(longest)