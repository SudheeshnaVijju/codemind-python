s=input().lower()
c=0
b=s.count('b')
n=s.count('n')
a=s.count('a')
o=s.count('o')
l=s.count('l')
while(b!=0 and n!=0 and a!=0 and l>=2 and o>=2):
    b-=1
    a-=1
    n-=1
    l-=2
    o-=2
    c+=1
print(c)