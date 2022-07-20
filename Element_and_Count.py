n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(len(a)):
        if (a[i] not in k ):
            k.append(a[i])
for i in k:
    print(i,end=' ')
    print(a.count(i),end=' ')
