n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
s=[]
for i in a:
    if(i>=x and i<=y):
        s.append(i)
if(len(s)>0):
    print(max(s))
else:
    print('-1')