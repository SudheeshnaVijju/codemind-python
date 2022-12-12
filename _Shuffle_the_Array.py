n=int(input())
a=list(map(int,input().split()))
k,l=int(input()),[]
for i in range(k):
    l.append(a[i])
    l.append(a[i+k])
print(*l)