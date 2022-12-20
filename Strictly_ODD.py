n=int(input())
a=list(map(int,input().split()))
for i in range(0,n,2):
    if(a[i]%2!=0):
        break
else:
    print('True')
    exit()
print(False)