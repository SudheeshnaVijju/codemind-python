n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if(a[i-1]%2!=0 and a[i+1]%2==0):
        c+=1
        #print(a[i-1],a[i+1])
    elif(a[i-1]%2==0 and a[i+1]%2!=0):
        c+=1
        #print(a[i-1],a[i+1])
if(a[0]%2!=0 and a[n-2]%2==0):
    c+=1
elif(a[0]%2==0 and a[n-2]%2!=0):
    c+=1
elif(a[n-1]%2==0 and a[1]%2!=0):c+=1
elif(a[n-1]%2!=0 and a[1]%2==0):c+=1
print(c)