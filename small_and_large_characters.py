s=input().lower().split()
for i in s:
    i=''.join(sorted(i))
    print(i[0],i[len(i)-1],end=' ')