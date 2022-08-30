def pan(n):
    t=n
    s=0
    while(n):
        s=s*10+(n%10)
        n//=10
    if(t==s):
        return 1
    return 0
n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    if(pan(i)):
        c+=1
print(c)