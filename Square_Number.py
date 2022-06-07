n=int(input())
c=0
i=0
while(i<25):
    for j in range(1,n+1):
        if(pow(i,2)+pow(j,2)==n and i!=j):
            c+=1
    i+=1
if(c>0):
    print(True)
else:
    print(False)