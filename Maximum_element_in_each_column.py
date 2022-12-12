n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(m):
    l=0
    for j in range(n):
        if(l<a[j][i]):l=a[j][i]
    print(l)
