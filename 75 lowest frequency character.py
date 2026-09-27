def lowest_frequency(text):
    lowest = len(text)
    character = ""
    for i in range(len(text)):
        count = 0
        for j in range(len(text)):
            if text[i] == text[j]:
                count = count + 1
        if count < lowest:
            lowest = count
            character = text[i]
    print("Lowest frequency character =", character)
    print("Frequency =", lowest)
text = input("Enter a string: ")
lowest_frequency(text)