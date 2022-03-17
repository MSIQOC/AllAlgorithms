def leftRotatebyOne(arr, n):
    first = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = first
    print(arr)
    return arr

arr = [1, 2, 3, 4, 5]
print(len(arr))
arrr = [0] * 3
print(len(arrr))
leftRotatebyOne(arr, len(arr))
