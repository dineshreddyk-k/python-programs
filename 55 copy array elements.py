def copy_array(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i)
    print("Copied array =", new_arr)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
copy_array(arr)