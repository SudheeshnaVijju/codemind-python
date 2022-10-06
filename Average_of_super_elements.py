n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k:
        k.append(i)
c=0
s=0
for i in k:
    if(a.count(i)==i):
        c+=i
        s+=1
if(s==0):
    print('-1')
else:
    print("%.2f"%(c/s))