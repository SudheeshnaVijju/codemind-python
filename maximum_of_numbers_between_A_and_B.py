n=int(input())
a=list(map(int,input().split()))
k=list(map(int,input().split()))
m=0
x=min(k)
y=max(k)
for i in a:
    if(i>=x and i<=y):
        if(m<i):
            m=i
if(m!=0):
    print(m)
else:
    print('-1')