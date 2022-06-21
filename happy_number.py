def ds(n):
    s=0
    while(n):
        s=s+pow((n%10),2)
        n//=10
    return s
def count(n):
    c=0
    while(n):
        c+=1
        n//=10
    return c

n=int(input())
s=ds(n)
while(True):
    if(count(s)>1):
        s=ds(s)
    else:
        if(s==1 or s==7):
            print("True")
        else:
            print('False')
        break
    