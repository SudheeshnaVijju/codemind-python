s1=input().lower().split()
s2=input().lower().split()
c=0
if len(s1)>len(s2):
    for i in s2:
        if i in s1 and s1.count(i)==1 and s2.count(i)==1:
            c+=1
    print(c)
    exit()
for i in s1:
    if i in s2 and s2.count(i)==1 and s1.count(i)==1:
        c+=1
print(c)