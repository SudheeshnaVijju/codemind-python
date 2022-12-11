n=int(input())
if(n==1 or n==2):
    print("2")
    exit()
a=[2,2]
i=0
while(i<n):
    a.append(a[i]+a[i+1])
    i+=1
print(a[n-1])