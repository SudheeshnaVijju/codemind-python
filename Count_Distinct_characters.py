s=input()
s=set(list(s.lower()))
c=0
for i in s:
    if(i==' '):
        c+=1
print(len(s)-c)