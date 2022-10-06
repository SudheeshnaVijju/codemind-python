n=int(input())
a=list(map(int,input().split()))
a=list(set(list(a)))
c=0
for i in a:
    if(i%2!=0 and a.count(i)==1):
        c+=1
print(c)