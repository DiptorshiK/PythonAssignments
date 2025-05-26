start=int(input("Enter The Starting Number Of The Range:"))
end=int(input("Enter The Ending Number Of The Range:"))

a,b=0,1
print("Fibonacci Series Of The Given Range Is:")
while a<=end:
    if a>=start:
        print(a,end=" ")
    a,b=b,a+b






