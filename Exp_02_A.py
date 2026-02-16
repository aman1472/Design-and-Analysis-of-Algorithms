import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


sizes = [100, 500, 1000, 3000, 5000]
times = []

for n in sizes:
    arr = list(range(n, 0, -1))  # Worst case
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    times.append(end - start)

plt.plot(sizes, times)
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Insertion Sort Time Complexity")
plt.show()
