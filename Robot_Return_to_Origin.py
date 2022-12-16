s,c=input(),0
for i in s:
    if(i=='L'):c+=-1
    if(i=='R'):c+=1
    if(i=='U'):c+=1
    if(i=='D'):c+=-1
if(c==0):print('True')
else:print(False)