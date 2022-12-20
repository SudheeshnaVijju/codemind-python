s=input().lower().split()
v='aeiou'
m,p=0,0
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    if(m<c):m=c
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    if(m==c):p+=1
print(p)
    