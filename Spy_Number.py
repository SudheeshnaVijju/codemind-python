n=int(input())
p=1
s=0
while(n!=0):
    d=n%10
    n=n//10
    s=s+d
    #print(s)
    p=p*d
if(p==s):
    print('Spy Number')
else:
    print('Not Spy Number')