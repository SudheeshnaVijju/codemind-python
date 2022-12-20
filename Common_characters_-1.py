s=input().lower().split()
k=s[0]
p=''
for i in k:
    for j in s:
        if i not in j:
            break
    else:
        p+=i
if(len(p)>0):
    print(p)
    exit()
print('-1')