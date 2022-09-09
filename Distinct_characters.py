s=input()
s=set(list(s.lower()))
k=''
for i in s:
    if(i!=' '):
        k+=i
k=''.join(sorted(k))
print(k)