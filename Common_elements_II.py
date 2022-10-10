n=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
m=[]
for i in a:
    if i not in l:
        l.append(i)
for i in b:
    if i not in m:
        m.append(i)
k=[]
for i in l:
    if i not in m:
        k.append(i)
for i in m:
    if i not in l:
        k.append(i)
for i in k:
    print(i,end=' ')