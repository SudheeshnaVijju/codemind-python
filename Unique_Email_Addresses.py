a=[]
for o in range(int(input())):
    s=input()
    k=''
    c,p=0,0
    for i in range(len(s)):
        if(s[i]=='+'):p+=1
        if(s[i]=='@'):
            c=1
        if(c!=1 and s[i]!='.' and p==0):
            k+=s[i]
        if(c==1):
            for j in range(i,len(s)-1):
                k+=s[j]
            break
        if(p==1):
            if(c==0):continue
    a.append(k)
a=set(list(a))
print(len(a))
            