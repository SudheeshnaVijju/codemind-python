n,m=map(int,input().split())
if(n>m):
    t=m
else:
    t=n
for i in range (t,0,-1):
    if(n%i==0 and m%i==0):
        print(i)
        break