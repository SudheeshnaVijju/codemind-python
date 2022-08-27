t=int(input())
for i in range(t):
    n=int(input())
    l=[]
    while(n):
        l.append(n%10)
        n//=10
    m=max(l)
    for j in range(min(l),m+1):
        if j not in l:
            print('NO')
            break
    else:
        print('YES')