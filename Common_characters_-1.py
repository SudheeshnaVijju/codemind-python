s=input().lower().split()
k,c,ns=s[0],0,''
for i in k:
    p=0
    for j in s:
        if i in j:
            p+=1
    if p==len(s):
        ns+=i
if ns=='':
    print('-1')
    exit()
print(ns)