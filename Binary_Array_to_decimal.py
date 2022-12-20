n=int(input())
a=list(map(int,input().split()))
c,d=0,0
for i in range(n-1,-1,-1):
    d=d+(a[i]*(2**c))
    c+=1
print(d)