n=int(input())
a=list(map(int,input().split()))
o,e,k=[],[],[]
for i in a:
    if(i%2==0):e.append(i)
    else:o.append(i)
i,j=0,0
while(i<len(o) or j<len(e)):
    if(i<len(o)):
        k.append(o[i])
    if(j<len(e)):k.append(e[i])
    i+=1
    j+=1
if(n%2!=0):k.append(0)
print(*k)