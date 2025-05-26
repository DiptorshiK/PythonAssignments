s = input("Enter a string : ")
print("The Count Of The Characters Are Listed Below !!")
for char in s:
    print(f"'{char}': {s.count(char)}")
