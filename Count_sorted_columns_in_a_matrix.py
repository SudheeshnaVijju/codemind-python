n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
c,s=0,0
for i in range(m):
    for j in range(n-1):
        if(a[j][i]>a[j+1][i]):break
    else:s+=1
for i in range(m):
    for j in range(n-1):
        if(a[j][i]<a[j+1][i]):break
    else:c+=1
print(c+s)