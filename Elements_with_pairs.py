n=int(input())
a=list(map(int,input().split()))
if(n%2!=0):
    for i in range(n):
        if(i!=n-1):
            print(a[i],end=' ')
        else:
            print(a[i],end=' 0')
else:
    for i in range(n):
        if((i)!=n-1):
            print(a[i],end=' ')
        else:
            print(a[i])