def count_substring(s, substring):
    return s.count(substring)
s=input("Enter the main string: ")
substring = "ab"

count = count_substring(s, substring)
print("Main string: ",s)
print("Substring to count: ",substring)
print("The substring ",substring,"appears",count," time(s) in the given string.")


