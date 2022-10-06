n=int(input())
a=list(map(int,input().split()))
k=list(map(int,input().split()))
x=min(k)
f=[]
y=max(k)
for i in a:
    if(i>=x and i<=y):
        f.append(i)
if(len(f)==0):
    print('-1')
else:
    print(min(f))