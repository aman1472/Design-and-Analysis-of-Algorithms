import time
import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


sizes = [1000, 3000, 5000, 7000, 10000]
times = []

for n in sizes:
    arr = list(range(n, 0, -1))  # Worst case
    start = time.time()
    merge_sort(arr)
    end = time.time()

    times.append(end - start)


plt.plot(sizes, times)
plt.xlabel("Input Size (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Merge Sort Time Complexity")
plt.show()
