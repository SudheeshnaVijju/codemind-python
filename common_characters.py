s1=list(input().lower())
s2=list(input().lower())
p='abcdefghijklmnopqrstuvwxyz'
s=''
for i in p:
    if i in s1 and i in s2:
        s+=i
if s=='':
    print('-1')
    exit()
print(s)