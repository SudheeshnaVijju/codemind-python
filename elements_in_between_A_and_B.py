n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
c=0
for i in a:
    if(i>=x and i<=y):
        print(i,end=' ')
        c=1
if(c==0):
    print('-1')