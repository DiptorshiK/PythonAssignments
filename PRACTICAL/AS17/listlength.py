s=input("Enter words separated by spaces: ")
l=s.split()
if len(l) == 0:
    print("Length of the longest word: 0")
else:
    max_length = 0
    for word in l:
        if len(word) > max_length:
            max_length = len(word)
    print("Length of the longest word:", max_length)
