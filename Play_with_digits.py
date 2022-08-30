n=int(input())
a=list(map(int,input().split()))
c=0
for i in a:
    t=i
    while(t):
        c+=t%10
        t//=10
print(c)