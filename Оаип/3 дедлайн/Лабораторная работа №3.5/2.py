import time
lst1 = list(range(100000))
start = time.time()
for _ in range(1000):
    lst1.pop(0)
print(f"pop(0): {time.time() - start:.4f} сек")
lst2 = list(range(100000))
start = time.time()
for _ in range(1000):
    lst2.pop()
print(f"pop(): {time.time() - start:.4f} сек")
# pop() быстрее O(1), pop(0) медленнее O(n)