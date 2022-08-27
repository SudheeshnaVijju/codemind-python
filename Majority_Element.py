n=int(input())
a=list(map(int,input().split()))
k=0
for i in a:
    if(k<a.count(i)):
        k=a.count(i)
for i in a:
    if(k==a.count(i)):
        print(i)
        break