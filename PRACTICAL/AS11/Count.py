s = input("Enter a string: ")
print("The Count Of The Characters Are Listed Below !!")

c={}

for char in s:
    if char in c:
        c[char] += 1
    else:
        c[char] = 1

# for char, count in c.items():
#     print(char,":",count)
print(c)
