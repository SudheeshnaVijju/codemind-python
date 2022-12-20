s=input().split()
i=s[0]
j=s[len(s)-1]
i=''.join(sorted(i))
j=''.join(sorted(j))
print(i[0],j[len(j)-1])