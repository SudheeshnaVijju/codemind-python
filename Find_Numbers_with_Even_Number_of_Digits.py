def dig(n):
    c=0
    while(n):
        n//=10
        c+=1
    return c
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(dig(i)%2==0):
        c+=1
print(c)