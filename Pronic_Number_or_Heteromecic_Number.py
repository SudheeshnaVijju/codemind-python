n=int(input())
c=0
for i in range(1,n):
    if(i*(i+1)==n):
        print('YES')
        c=1
        break
if c!=1:
    print('NO')
    