s1=list(input().lower())
s2=list(input().lower())
p='abcdefghijklmnopqrstuvwxyz'
s=''
for i in p:
    if i not in s1 and i in s2 or i in s1 and i not in s2:
        s+=i
print(s)