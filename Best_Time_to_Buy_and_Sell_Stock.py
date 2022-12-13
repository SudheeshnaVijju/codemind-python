n=int(input())
a=list(map(int,input().split()))
m=0
for i in range(n):
    for j in range(i+1,n):
        if(a[j]>a[i] and m<a[j]-a[i]):
            m=a[j]-a[i]
print(m)