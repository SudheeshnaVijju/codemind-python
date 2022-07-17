n=int(input())
a=list(map(int,input().split()))
a=list(set(a))
s=0
for i in a:
    s+=i
print(s)