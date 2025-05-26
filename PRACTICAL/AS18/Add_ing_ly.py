s=input("Enter A String : ")
if len(s)<3:
     print(s,", It Goes Unchanged !!")

 
elif s.endswith("ing"):
     print(s+"ly")

else:
     print(s+"ing")




