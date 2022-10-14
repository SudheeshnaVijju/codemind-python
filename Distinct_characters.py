s=list(input().lower())
while ' ' in s:
    s.remove(' ')
print(''.join(sorted(set(s))))