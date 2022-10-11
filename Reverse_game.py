n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    c.append(int(str(i)[::-1]))
print(*c)