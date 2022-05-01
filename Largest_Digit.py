t=int(input())
s=0
while(t!=0):
    d=t%10
    t=t//10
    if(s<d):
        s=d
print(s)