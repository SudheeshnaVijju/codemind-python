n=int(input())
a=list(map(int,input().split()))
s=0
p=0
for i in range(n//2):
    s+=a[i]
for i in range(n//2,n):
    p+=a[i]
print(s)
print(p)