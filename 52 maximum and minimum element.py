def maximum_minimum(arr):
    maximum = arr[0]
    minimum = arr[0]
    for i in arr:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
    print("Maximum =", maximum)
    print("Minimum =", minimum)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
maximum_minimum(arr)