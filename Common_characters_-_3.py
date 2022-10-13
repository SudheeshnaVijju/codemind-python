s=input().lower().split()
p='abcdefghijklmnopqrstuvwxyz'
k=0
for i in p:
    k=0
    for j in s:
        if i in j:
            k+=1
    if(k==len(s)):
        print(i)
        exit()
print('-1')