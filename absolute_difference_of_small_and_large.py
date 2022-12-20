s=input().split()
a=[]
for i in s:
    m=0
    i=''.join(sorted(i))
    a.append(abs(ord(i[0])-ord(i[len(i)-1])))
print(*a)