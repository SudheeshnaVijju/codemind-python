s=input().lower().split()
m=1000
p=0
v='aeiou'
for i in s:
    c=0
    for j in i:
        if(j in v):
            c+=1
    if(m>c):m=c
for i in s:
    c=0
    for j in i:
        if(j in v):
            c+=1
    if(m==c):p+=1
print(p)
