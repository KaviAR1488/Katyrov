import time, random
def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                duplicates.append(arr[i])
    return duplicates
n = 5000
arr1 = [random.randint(1, 100) for _ in range(n)]
start = time.time()
find_duplicates(arr1)
t1 = time.time() - start
arr2 = [random.randint(1, 100) for _ in range(n * 2)]
start = time.time()
find_duplicates(arr2)
t2 = time.time() - start
print(f"n={n}: {t1:.4f} сек")
print(f"n={n*2}: {t2:.4f} сек")
print(f"Увеличилось в {t2 / t1:.2f} раз")
# При увеличении данных в 2 раза время выросло примерно в 4 раза