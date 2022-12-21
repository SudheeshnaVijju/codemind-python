s=input()
a,m=[],[]
for i in range(len(s)):
    for j in range(i,len(s)):
        l=set(list(s[i:j].lower()))
       # print(l)
        if(len(l)==len(s[i:j])):
            a.append(s[i:j])
            m.append(len(s[i:j]))
#print(*a)
if(max(m)<3):
    print('-1')
    exit()
for i in a:
    if(max(m)==len(i)):
        print(i)
        exit()
        break
