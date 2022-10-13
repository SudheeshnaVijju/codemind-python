s=input().split()
mx,mi=0,0
for i in s:
    mx=mx+ord(max(i))
    mi=mi+ord(min(i))
print(mx-mi)