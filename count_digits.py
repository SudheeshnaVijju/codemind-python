n=int(input())
a=list(map(int,input().split()))
c=[]
for i in a:
    c.append(len(str(abs(i))))
print(*c)