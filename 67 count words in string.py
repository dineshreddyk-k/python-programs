def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        count = count + 1
    print("Number of words =", count)
text = input("Enter a string: ")
count_words(text)