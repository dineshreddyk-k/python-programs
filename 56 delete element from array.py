def delete_element(arr, position):
    for i in range(position, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    print("Array after deletion =", arr)
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
position = int(input("Enter position to delete: "))
delete_element(arr, position)