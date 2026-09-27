def negative_elements(arr):
    for i in arr:
        if i < 0:
            print(i)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
negative_elements(arr)