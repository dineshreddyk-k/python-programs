def missing_number(arr, n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    for i in arr:
        total = total - i
    print("Missing number =", total)
arr = []
n = int(input("Enter last number: "))
for i in range(n - 1):
    value = int(input("Enter number: "))
    arr.append(value)
missing_number(arr, n)