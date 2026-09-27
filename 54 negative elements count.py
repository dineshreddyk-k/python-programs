def count_negative(arr):
    count = 0
    for i in arr:
        if i < 0:
            count = count + 1
    print("Negative elements =", count)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
count_negative(arr)