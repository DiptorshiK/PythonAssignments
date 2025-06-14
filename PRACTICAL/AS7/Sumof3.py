a=int(input("Enter The First Number:"))
b=int(input("Enter The Second Number:"))
c=int(input("Enter The Third Number:"))

Sum=0

if a==b or b==c or a==c :
    print("The Sum Is Zero.")
else:
    Sum=a+b+c
    print(Sum,"Is The Sum Of The Three Numbers.")