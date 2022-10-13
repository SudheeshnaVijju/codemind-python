p=input().split()
v='aeiouAEUIO'
c=0
for s in p:
    j,i=len(s)-1,0
    while(i<j):
        if(s[i] in v and s[j] not in v) or (s[i] not in v and s[j] in v):
            c+=1
        i+=1
        j-=1
print(c)