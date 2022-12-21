n,m=map(int,input().split())
r,c=[],[]
a=[]
for i in range(m):a.append(0)
for i in range(n):
    b=list(map(int,input().split()))
    r.append(sum(b))
    for j in range(m):
        l=a[j]
        a.remove(a[j])
        a.insert(j,b[j]+l)
print(max(max(a),max(r)))