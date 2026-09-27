def reverse_array(arr):
    reverse = []
    for i in range(len(arr) - 1, -1, -1):
        reverse.append(arr[i])
    print("Reverse array =", reverse)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
reverse_array(arr)