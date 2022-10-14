s=input().split()
k,p=0,[]
for i in s:
    p.append(len(list(i)))
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]>p[j]:
            s[i],s[j]=s[j],s[i]
            p[i],p[j]=p[j],p[i]
        if(p[i]==p[j] and s[i]>s[j]):
            s[i],s[j]=s[j],s[i]
print(*s)