n=int(input())
a=list(map(int,input().split()))
e,o,k=[],[],[]
for i in a:
    if(i%2==0):e.append(i)
    else:o.append(i)
i=0
j=0
while(i<len(e) or j<len(o)):
    if(i<len(e)):
        k.append(e[i])
    if(j<len(o)):
        k.append(o[i])
    i+=1
    j+=1
if(n%2!=0):k.append(0)
print(*k)