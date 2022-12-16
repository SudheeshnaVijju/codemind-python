s=input()
k=s.split()
a='aeiouAEIOU'
for i in range(len(k)):
    if(k[i][0] in a):k[i]=k[i]+'ma'
    else:k[i]=k[i][1:len(k[i])]+k[i][0]+'ma'
for i in range(len(k)):
    c=i+1
    while(c):
        k[i]+='a'
        c-=1
print(*k)
        