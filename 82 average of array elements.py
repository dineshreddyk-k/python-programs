def average(arr):
    total = 0
    for i in arr:
        total = total + i
    result = total / len(arr)
    print("Average =", result)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
average(arr)