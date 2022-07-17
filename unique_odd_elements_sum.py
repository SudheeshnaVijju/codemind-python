
n=int(input())
a=list(map(int,input().split()))
s=0
a=list(set(a))
for i in a:
    if(i%2!=0):
        s+=i



print(s)