def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1


arr1 = [64, 34, 25, 12, 22, 11, 90, 89]
insertion_sort(arr1)
print(arr1)
