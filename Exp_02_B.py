import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


sizes = [100, 500, 1000, 3000, 5000]
times = []

for n in sizes:
    arr = list(range(n, 0, -1))  # Worst case
    start = time.time()
    bubble_sort(arr)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times)
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Bubble Sort Time Complexity")
plt.show()
