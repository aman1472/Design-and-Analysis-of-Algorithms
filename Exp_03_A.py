import time
import matplotlib.pyplot as plt

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


sizes = [1000, 3000, 5000, 7000, 10000]
times = []

for n in sizes:
    arr = list(range(n, 0, -1))  # Worst/Average case
    start = time.time()
    quick_sort(arr)
    end = time.time()

    times.append(end - start)


plt.plot(sizes, times)
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Quick Sort Time Complexity")
plt.show()
