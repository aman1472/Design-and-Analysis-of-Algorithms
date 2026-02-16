import time
import matplotlib.pyplot as plt

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


sizes = [100, 500, 1000, 3000, 5000]
times = []

for n in sizes:
    arr = list(range(n, 0, -1))  # Worst case
    start = time.time()
    selection_sort(arr)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times)
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Selection Sort Time Complexity")
plt.show()
