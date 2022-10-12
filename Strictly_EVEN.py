n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    if(i%2!=0 and a[i]%2==0):
        print('False')
        break
else:
    print("True")
        
'''for i in range(n):
    if(i%2==0 and a[i]%2!=0):
        print('false')
        break
else:
    print('True')'''
        