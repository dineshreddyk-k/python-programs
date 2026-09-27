def duplicate_elements(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count = count + 1
        if count > 1 and arr[i] not in arr[:i]:
            print(arr[i])
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
duplicate_elements(arr)