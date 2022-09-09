s=input()
s=s.lower()
s=list(s)
c=0
for i in s:
    if(s.count(i)==1 and i!=' '):
        c+=1
print(c)