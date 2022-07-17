n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
s=0

for i in a:
    if(i%2==0):
        s+=i
print(s)