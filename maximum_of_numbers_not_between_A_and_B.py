n=int(input())
a=list(map(int,input().split()))
p,q=map(int,input().split())
k=[]
for i in a:
    if(i<p or i>q):k.append(i)
if(len(k)>0):
    print(max(k))
    exit()
print('-1')