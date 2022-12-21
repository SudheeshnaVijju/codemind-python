n,m=map(int,input().split())
a=[]
for i in range(1,n+1):a.append(i)
from itertools import permutations
p=list(permutations(a))
for i in p[m-1]:
    print(i,end='')