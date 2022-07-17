def dc(n):
    s=0
    while(n):
        n//=10
        s+=1
    return s
n=int(input())
a=list(map(int,input().split()))
m=min(a)
c=0
s=0
while(m):
    m//=10
    c+=1
for i in a:
    if(dc(i)==c):
        s+=1
print(s)