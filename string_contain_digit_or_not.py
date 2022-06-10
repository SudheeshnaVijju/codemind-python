s=input()
a='1234567890'
c=0
for i in s:
    for j in a:
        if (j==i):
            c+=1
if(c>0):
    print('Contains',c,'digit')
else:
    print("Doesn't contain digit")