s=input()
c=0
for i in s:
    if(i!=' ' and ord(i)>=65 and ord(i)<=90):
        c+=1
print(c)