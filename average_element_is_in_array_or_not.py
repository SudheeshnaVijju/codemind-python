n=int(input())
ls=list(map(int,input().split()))
if sum(ls)//n in ls:
    print("True")
else:
    print("False")