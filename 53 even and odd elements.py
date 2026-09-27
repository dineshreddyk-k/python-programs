def count_even_odd(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print("Even elements =", even)
    print("Odd elements =", odd)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
count_even_odd(arr)