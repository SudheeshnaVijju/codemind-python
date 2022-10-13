s1=list(input().lower())
s2=list(input().lower())
p='abcdefghijklmnopqrstuvwxyz'
s=0
for i in p:
    if i in s1 and i in s2:
        s+=1
print(s)