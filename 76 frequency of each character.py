def frequency(text):
    for i in range(len(text)):
        count = 0
        for j in range(len(text)):
            if text[i] == text[j]:
                count = count + 1
        if text[i] not in text[:i]:
            print(text[i], ":", count)
text = input("Enter a string: ")
frequency(text)