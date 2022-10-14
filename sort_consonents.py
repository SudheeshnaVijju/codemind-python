v='aeiouAEIOU'
s=input().split()
for i in s:
    x,s=[],''
    for j in i:
        if j not in v:
            x.append(j)
    x=sorted(x)
    p=0
    for k in range(len(i)):
        if i[k] not in v:
            s+=x[p]
            p+=1
        else:
            s+=i[k]
    print(s,end=' ')