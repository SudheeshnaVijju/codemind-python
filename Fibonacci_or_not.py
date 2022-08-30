n=int(input())
x=0
y=1
while(1):
    if(n==0 or n==1):
        print('True')
        break
    else:
        t=x
        x=x+y
        if(x==n):
            print(True)
            break
        elif(x>n):
            print(False)
            break
        y=t