for o in range(int(input())):
    s=input()
    c=0
    d=0
    for i in range(len(s)-1,-1,-1):
        d=d+(int(s[i])*2**c)
        c+=1
    print(d)