s=input()
a='aeiou'
c=0
b=''
for i in s:
    if i in a:
        b=b+i
for i in a:
    if (i in a and i not in b):
        print(i,end=' ')
        c=1
if(c!=1):
    print('0')
        