n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k:
        k.append(i)
c=0
for i in k:
    if(a.count(i)==i):
        print(i,end=' ')
        c=1
if(c==0):
    print('-1')