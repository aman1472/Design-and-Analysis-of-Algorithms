def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


unsorted_data = [12, 44, 32, 18, 4, 10]
sorted_data = [4, 10, 12, 18, 32, 44]
print("Linear Search:", linear_search(unsorted_data, 18))
print("Binary Search:", binary_search(sorted_data, 18))
