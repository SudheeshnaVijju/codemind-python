a,b=map(int,input().split())
ls1=list(map(int,input().split()))
ls2=list(map(int,input().split()))
for i in ls2:
    if i not in ls1:
        print("No")
        exit()
    ls1.remove(i)
print("Yes")