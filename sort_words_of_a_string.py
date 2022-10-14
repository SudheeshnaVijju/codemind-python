v='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s=input().split()
for i in s:
    x,s=[],''
    for j in i:
        if j in v:
            x.append(j)
    x=sorted(x)
    p=0
    for k in range(len(i)):
        if i[k] in v:
            s+=x[p]
            p+=1
        else:
            s+=i[k]
    print(s,end=' ')