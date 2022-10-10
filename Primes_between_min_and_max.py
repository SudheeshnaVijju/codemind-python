from math import sqrt
def prime(n):
    if(n==0):
        return 0
    if(n==1):
        return 0
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
a=list(map(int,input().split()))
m=a.index(min(a))
ma=a.index(max(a))
c=0
if(m>ma):
    m,ma=ma,m
for i in range(m,ma+1):
    #if(i>=m and i<=ma and prime(i)):
    if(prime(a[i]) and a[i]>0):
        c+=1
print(c)
#print(m,ma)
    