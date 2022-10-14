from math import sqrt
def isf(n):
    k=0
    arr=[k]
    a=0
    b=1
    c=a+b
    while(c<n):
        arr.remove(k)
        arr.append(c)
        k=c
        a=b
        b=c
        c=a+b
    arr.append(c)
    return arr
n=int(input())
p=isf(n)
if(n-p[0]==p[1]-n):
    print(p[0],end=' ')
    print(p[1],end='')
elif(n-p[0]<p[1]-n):
    print(p[0])
elif(n-p[0]>p[1]-n):
    print(p[1])