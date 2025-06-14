i=(input("Enter A Single Letter Alphabet:"))

if len(i)==1 and i.isalpha():
    if i.lower() in 'a,e,i,o,u':
        print(i,"Is A Vowel.")
    else:
        print(i,"Is Not A Vowel.")


else:
    print("Invalid Input , It May Not Be A Single Word. Therefore Please Enter A Single Letter. ")



