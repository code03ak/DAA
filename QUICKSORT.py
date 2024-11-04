import random, time

def quick_sort(arr, randomized=False):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1) if randomized else len(arr) - 1
    pivot = arr[pivot_index]
    less = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less, randomized) + [pivot] + quick_sort(greater, randomized)

# Input
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Deterministic Quick Sort (run multiple times for precision)
start = time.perf_counter()
for _ in range(10000):  # Repeat to get measurable time
    sorted_det = quick_sort(arr)
det_time = (time.perf_counter() - start) / 10000  # Average time per sort

# Randomized Quick Sort (run multiple times for precision)
start = time.perf_counter()
for _ in range(10000):  # Repeat to get measurable time
    sorted_rand = quick_sort(arr, randomized=True)
rand_time = (time.perf_counter() - start) / 10000  # Average time per sort

# Output
print(f"Sorted array using deterministic Quick Sort: {sorted_det}")
print(f"Average time taken (deterministic): {det_time:.8f} seconds")
print(f"Sorted array using randomized Quick Sort: {sorted_rand}")
print(f"Average time taken (randomized): {rand_time:.8f} seconds")
