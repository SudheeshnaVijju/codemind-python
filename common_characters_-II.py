s1=input().lower()
s2=input().lower()
k=''
c=0
for i in s1:
    if i in s2 and i!=' ':
        k+=i
        c+=1
print(len(set(k)))