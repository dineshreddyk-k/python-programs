def common_elements(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                print(i)
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
common_elements(arr1, arr2)