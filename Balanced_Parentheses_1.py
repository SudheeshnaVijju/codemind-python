s=input()
a=[]
for i in s:
    if i=='(' or i=='{' or i=='[':
        a.append(i)
    else:
        if(i==')'):
            if '(' in a:
                a.remove('(')
            else:
                print(False)
                exit()
        if(i=='}'):
            if '{' in a:
                a.remove('{')
            else:
                print(False)
                exit()
        if(i==']'):
            if '[' in a:
                a.remove('[')
            else:
                print(False)
                exit()
if(len(a)==0):print(True)
else:print(False)
            
        