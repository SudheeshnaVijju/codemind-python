n=int(input())
a=list(map(int,input().split()))
m=[]
for i in range(n):
    s=0
    for j in range(i,n):
        s+=a[j]
        m.append(s)
print(max(m))
        