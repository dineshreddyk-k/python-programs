def highest_frequency(text):
    highest = 0
    character = ""
    for i in range(len(text)):
        count = 0
        for j in range(len(text)):
            if text[i] == text[j]:
                count = count + 1
        if count > highest:
            highest = count
            character = text[i]
    print("Highest frequency character =", character)
    print("Frequency =", highest)
text = input("Enter a string: ")
highest_frequency(text)