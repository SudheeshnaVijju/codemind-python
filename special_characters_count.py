s=input()
c=0
for i in s:
    if(ord(i)>=97 and ord(i)<=122 or i==' '):
        continue
    elif(ord(i)>=65 and ord(i)<=90):
        continue
    else:
        c+=1
print(c)