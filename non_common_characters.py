s1=input().lower()
s2=input().lower()
k=''
for i in s1:
    if i not in s2 and i!=' ':
        k+=i
for i in s2:
    if i not in s1 and i!=' ':
        k+=i
k=set(k)
print(''.join(sorted(k)))