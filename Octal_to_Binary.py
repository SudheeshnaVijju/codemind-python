for o in range(int(input())):
    n=int(input())
    d=0
    n=str(n)
    c=len(n)-1
    i=0
    while(i<len(n)):
        d=d+(int(n[i])*(8**c))
        c-=1
        i+=1
    s=''
    while(d):
        s=str((d%2))+s
        d//=2
    print(int(s))
        