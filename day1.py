import sys

f = file('input')
s = f.read()
floor = 0
cnt = 0
for c in s:
    cnt += 1
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
        if floor == -1:
            print cnt
            sys.exit(0)
print floor

    
