n=int(input())
a=list(map(int,input().split()))
o=[]
e=[]
for i in a:
    if(i%2==0):e.append(i)
    else:o.append(i)
o.extend(e)
print(*o)