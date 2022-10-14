s=list(input().lower())
p='abcdefghijklmnopqrstuvwxyz'
ns=''
while ' ' in s:
    s.remove(' ')
for i in p:
    if s.count(i)==1:
        ns=ns+i
print(ns)