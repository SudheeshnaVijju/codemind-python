n,m=map(int,input().split())
a=[]
s,k=0,0
for i in range(n):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(n):
    for j in range(m-1):
        if(a[i][j]>a[i][j+1]):
            break
    else:s+=1
for i in range(n):
    for j in range(m-1):
        if(a[i][j]<a[i][j+1]):
            break
    else:k+=1
print(k+s)