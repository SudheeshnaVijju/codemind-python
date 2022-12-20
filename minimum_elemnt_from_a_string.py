s=input().split()
s=s[len(s)-1]

s=''.join(sorted(s))
s=s[0:2]
if(ord(s[1])-ord(s[0])==32):
    print(s[1])
else:
    print(s[0])