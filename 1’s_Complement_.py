n=int(input())
b=bin(n)[2:]
i=0
a=''
while(len(b)-1>=i):
    if(b[i]=='0'):
       a+='1'
    else:
        a+='0'
    i+=1
print(int(a,2))