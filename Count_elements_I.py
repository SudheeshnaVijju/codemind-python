n=list(map(int,input().split()))
a=list(map(int,input().split()))
a=set(list(a))
b=list(map(int,input().split()))
c=0
for i in a:
    if i in b:
        c+=1
print(c)