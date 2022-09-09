s=input()
s=s.lower()
a='aeiou'
k=''
for i in s:
    if(i in a):
        k+=i
c=0
for i in a:
    if i not in k:
        print(i,end=' ')
        c=1
if(c==0):
    print('0')