s1=input().lower()
s2,k=input().lower(),''
s,p='',''
for i in s1:
    s+=i
for i in s2:
    p+=i
for i in s:
    if i in p and i!=' ':
        k+=i
k=set(k)
if(len(k)>0):
    print(''.join(sorted(k)))
else:
    print("-1")