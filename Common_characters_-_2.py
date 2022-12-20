s=input().lower().split()
k=s[0]
p=''
for i in k:
    c=0
    for j in s:
        if i not in j:
            break
    else:
        p+=i
print(len(p))
