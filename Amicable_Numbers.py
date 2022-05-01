n=int(input())
m=int(input())
s=0
c=0
for i in range (1,n):
    if(n%i==0):
        s=s+i
for i in range (1,m):
    if(m%i==0):
        c=c+i
if(c==n and s==m):
    print('Amicable')
else:
    print('Not Amicable')