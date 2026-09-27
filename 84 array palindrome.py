def palindrome(arr):
    reverse = []
    for i in range(len(arr) - 1, -1, -1):
        reverse.append(arr[i])
    if arr == reverse:
        print("Palindrome")
    else:
        print("Not a Palindrome")
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
palindrome(arr)