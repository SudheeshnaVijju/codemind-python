def prime(n):
    if(n==1):return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
m=min(a)
ma=max(a)
c=0
i=a.index(m)
j=a.index(ma)
if(i>j):i,j=j,i
for o in range(i,j+1):
    if(prime(a[o])):c+=1
print(c)