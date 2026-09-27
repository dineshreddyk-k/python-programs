def second_largest(arr):
    largest = arr[0]
    second = arr[0]
    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    print("Second largest =", second)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
second_largest(arr)