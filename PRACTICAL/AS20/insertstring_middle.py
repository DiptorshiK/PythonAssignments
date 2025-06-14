s = input("Enter a string: ")
s2 = input("Enter the string to insert in the middle: ")
mid = len(s) // 2
result = s[:mid] +" "+ s2 +" "+ s[mid:]
print("Result:", result)
