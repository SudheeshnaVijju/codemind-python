s=input().split()
for i in s:
    mx,mi=0,0
    mx=mx+ord(max(i))
    mi=mi+ord(min(i))
    print(abs(mx-mi),end=' ')