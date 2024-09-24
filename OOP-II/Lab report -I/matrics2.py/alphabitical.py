string = input("Enter a string: ")
words = string.split()
words.sort()
print("Sorted words in alphabetical order:")
for word in words:
    print(word)
