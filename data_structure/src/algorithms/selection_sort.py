arr = [3, 2, 10, 4, 3, 20, 38]

for i in range(1, len(arr)):
    key = i
    while arr[key-1] > arr[key] and key >= 1:
        arr[key-1], arr[key] = arr[key], arr[key-1]
        key -= 1
print(arr)