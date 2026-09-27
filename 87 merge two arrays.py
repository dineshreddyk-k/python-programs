def merge_array(arr1, arr2):
    result = []
    for i in arr1:
        result.append(i)
    for i in arr2:
        result.append(i)
    print("Merged array =", result)
arr1 = []
arr2 = []
n = int(input("Enter number of elements in first array: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr1.append(value)
n = int(input("Enter number of elements in second array: "))
for i in range(n):
    value = int(input("Enter element: "))
    arr2.append(value)
merge_array(arr1, arr2)