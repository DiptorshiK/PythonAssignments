def check_numbers(a,b):
    if a==b or a+b==5 or a-b==5 or b-a==5:
        return True
    else:
        return False
    

a=int(input("Enter The First Number:"))
b=int(input("Enter The Second Number:"))

print(check_numbers(a,b))
