def duplicate_elements(arr):
    count = 0
    for i in range(len(arr)):
        frequency = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                frequency = frequency + 1
        if frequency > 1 and arr[i] not in arr[:i]:
            count = count + 1
    print("Duplicate elements =", count)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
duplicate_elements(arr)