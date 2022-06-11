l=int(input())
t=int(input())
for i in range(t):
    w,h=map(int,input().split())
    if(w<l or h<l):
        print('UPLOAD ANOTHER')
    elif(w==h):
        print('ACCEPTED')
    elif(w>l or h>l):
        print('CROP IT')
    #print(w,h,l)