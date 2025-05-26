def fun(s):
    tl = s.lower()
    n=tl.find('not')
    p=tl.find('poor')

    try:
       
        if p > n >= 0:
            return s[:n] + 'Good' + s[p + 4:]
    except:
        pass

    return s
s=input("Enter A Sentence : ")
print("result:",fun(s))