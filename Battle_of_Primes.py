def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
m=int(input())
i=1
while(1):
    if(prime(n+m+i)):
        print(i)
        break
    i+=1