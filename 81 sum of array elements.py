def array_sum(arr):
    total = 0
    for i in arr:
        total = total + i
    print("Sum =", total)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
array_sum(arr)