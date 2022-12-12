a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
p=0
for i in range(3):
    if(a[i]>b[i]):k+=1
    elif(b[i]>a[i]):p+=1
print(k,p)