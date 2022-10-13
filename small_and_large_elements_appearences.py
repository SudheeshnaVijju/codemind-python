s=list(input())
while " " in s:
    s.remove(' ')
print(min(s),s.count(min(s)),end=' ')
print(max(s),s.count(max(s)),end=' ')