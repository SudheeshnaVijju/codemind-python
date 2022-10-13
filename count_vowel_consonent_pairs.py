s=input()
v='aeuioAEUIO'
j,c,i=len(s)-1,0,0
while(i<j):
    if s[i]==' ' or s[j]==' ':
        i+=1
        j-=1
        continue
    if(s[i] in v and s[j] not in v) or (s[i] not in v and s[j] in v):
        c+=1
    i+=1
    j-=1
print(c)