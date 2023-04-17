def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    bubbleSort(arr)
    print(arr)


arr1 = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr1)
print('\n', arr1)
