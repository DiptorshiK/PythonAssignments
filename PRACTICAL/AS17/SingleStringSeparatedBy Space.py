def string_swap(s1,s2):
    if len(s1)<2 or len(s2)<2:
        print("It Can Not Be Swapped !! , Give String Of Length Atleast More Than 2")

    else:

        ns1=s2[:2]+s1[2:]
        ns2=s1[:2]+s2[2:]
        result=ns1+" "+ns2 
        return result

s1=input("Enter Any String 1 : ")
s2=input("Enter Any String 2 : ")


result1=string_swap(s1,s2)
print(result1)