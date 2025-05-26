def count_substring_occurrences(s, substring):
    return s.count(substring)
s=input("Enter the main string: ")
substring = "ab"

count = count_substring_occurrences(s, substring)
print(f"Main string: '{s}'")
print(f"Substring to count: '{substring}'")
print(f"The substring '{substring}' appears {count} time(s) in the given string.")


