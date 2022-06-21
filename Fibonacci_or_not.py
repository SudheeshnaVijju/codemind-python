n=int(input())
x=0
y=1
while(n):
    if(n==x or n==y):
        print('True')
        break
    else:
        t=x
        x=y+x
        y=t
        if(n==x):
            print('True')
            break
        elif(n<x):
            print('False')
            break