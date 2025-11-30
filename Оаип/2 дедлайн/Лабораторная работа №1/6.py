char = input()
height = int(input())
width = int(input())
i = 0
while i < height:
    j = 0
    while j < width:
        print(char, end="")
        j += 1
    print()
    i += 1