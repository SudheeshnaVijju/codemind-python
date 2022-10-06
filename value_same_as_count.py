n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k:
        k.append(i)
c=0
for i in k:
    if(i==a.count(i)):
        c+=1
print(c)