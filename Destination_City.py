n=int(input())
a=[]
for i in range(n):
    b=list(map(str,input().split()))
    a.append(b)
for i in range(n):
    c=0
    for j in range(n):
        if(a[i][1]==a[j][0]):
            c+=1
    if(c==0):
        print(a[i][1])
        break
    