n=int(input())
a=list(map(int,input().split()))
k=[]
for i in a:
    if i not in k:
        k.append(i)
for i in range(len(k)):
    if(i!=len(k)-1):
        print(k[i],end=' ')
        print(a.count(k[i]),end=' ')
    else:
        print(k[i],end=' ')
        print(a.count(k[i]))