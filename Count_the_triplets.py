for o in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if(a[i]+a[j] in a):
                c+=1
    if(c>0):
        print(c)
    else:print('-1')