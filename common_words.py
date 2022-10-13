s1=input().lower().split()
s2=input().lower().split()
f,x=-1,[]
for i in s2:
    for j in s1:
        if i==j:
            print(i,end=' ')