n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append(0)
for i in range(n):
    b=list(map(int,input().split()))
    for k in range(m):
        l=a[k]
        a.remove(a[k])
        a.insert(k,l+b[k])
print(*(a))