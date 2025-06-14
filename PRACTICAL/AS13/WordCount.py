s=input("Enter a sentence: ")
word=s.split()

for w in set(word):
   print(w, ":", word.count(w))
