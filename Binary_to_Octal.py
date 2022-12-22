for o in range(int(input())):
    n=int(input())
    n=str(n)
    d=0
    c=len(n)-1
    i=0
    while(i<len(n)):
        d=d+(int(n[i])*(2**c))
        c-=1
        i+=1
    s=''
    while(d):
       s=str(d%8)+s
       d//=8
    print(int(s))