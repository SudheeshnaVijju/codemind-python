n=int(input())
a=list(map(int,input().split()))
k=list(map(int,input().split()))
x=min(k)
y=max(k)
f=[]
for i in a:
    if(i<x or i>y):
        f.append(i)
if(len(f)==0):
    print('-1')
else:
    print(min(f))