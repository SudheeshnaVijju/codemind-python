n=int(input())
N=list(map(int,input().split()))
s=0
for i in N:
    if(i%2==0):
        s+=1
print(s,n-s)
        
