n,m=map(int,input().split())
a=list(map(int,input().split()))
while(m):
    s=a[0]
    a.remove(s)
    a.append(s)
    #print(*a)
    m-=1
print(*a)