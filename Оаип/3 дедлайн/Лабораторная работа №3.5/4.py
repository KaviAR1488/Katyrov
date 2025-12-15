import time, random
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None
def find_pair_fast(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen.add(num)
    return None
arr = [random.randint(1, 10000) for _ in range(10000)]
target = 15000
start = time.time()
result_slow = find_pair_slow(arr, target)
print(f"Медленно: {time.time() - start:.4f} сек")
start = time.time()
result_fast = find_pair_fast(arr, target)
print(f"Быстро: {time.time() - start:.4f} сек")