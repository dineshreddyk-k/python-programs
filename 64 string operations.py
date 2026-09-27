def string_operations(str1, str2):
    print("Length of first string =", len(str1))
    print("Length of second string =", len(str2))
    if str1 == str2:
        print("Both strings are same")
    else:
        print("Both strings are different")
    result = str1 + str2
    print("Concatenated string =", result)
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
string_operations(str1, str2)