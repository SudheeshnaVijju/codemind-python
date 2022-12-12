for o in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=a[j]
            if(s==k):
                print(i+1,j+1)
                break
        if(s==k):
            break
    else:
        print('-1')