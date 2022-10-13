k=input().split()
s=k[len(k)-1]
m='z'
for i in s:
    if(i<m):
        m=i
if m.lower() in s:
    m=m.lower()
print(m)