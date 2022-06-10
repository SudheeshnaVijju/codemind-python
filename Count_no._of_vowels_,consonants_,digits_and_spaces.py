s=input()
v='aeiouAEIOU'
c='qwrtyplkjhgfdszxcvbnmPYTRWQSDFGHJKLZXCVBNM'
n='1234567890'
V=0
C=0
N=0
a=0
for i in s:
    if i in v:
        V+=1
    elif i in c:
        C+=1
    elif i in n:
        N+=1
    elif(i==' '):
        a+=1
print("Vowels:",V)
print("Consonants:",C)
print("Digits:",N)
print("White spaces:",a)