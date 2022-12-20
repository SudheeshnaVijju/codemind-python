n=int(input())
a=list(map(int,input().split()))
if(a.count(0)+a.count(1)==n):
    print(True)
    exit()
print(False)