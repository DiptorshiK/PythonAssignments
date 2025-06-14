def fun(s):
    if len(s) < 2:
        return " "  
    else:
        return s[:2] + s[-2:]

s=input("Enter A String : ")
result = fun(s)
print("Result:", result)


