def delete_element(arr, position):
    if position >= 0 and position < len(arr):
        arr.pop(position)
        print("Array after deletion =", arr)
    else:
        print("Invalid position")
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
position = int(input("Enter position to delete: "))
delete_element(arr, position)