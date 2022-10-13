s=input()
s=s.split()
for i in range(len(s)):
    if(i%2==0):
        p=s[i]
        s[i]=p[::-1]
print(*s)