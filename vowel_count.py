s=input()
c=0
a='AEIOUaeiou'
for i in s:
    if i in a:
        c+=1
print(c)