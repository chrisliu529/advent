def inc_letter_(c):
    return chr(ord(c)+1)

def inc_letter(c):
    if c < 'z':
        return inc_letter_(c), False
    return 'a', True

def inc2(p, n):
    if n == 0:
        return ''
    c, over = inc_letter(p[n])
    if over:
        return inc2(p[:-1], n-1) + c
    return p[:-1] + c

def inc(p):
    return inc2(p, len(p)-1)

def is_straight(s):
    return s[1] == inc_letter_(s[0]) and s[2] == inc_letter_(s[1])

def straight(p, n):
    for i in range(len(p)-n):
        if is_straight(p[i:i+n]):
            return True
    return False

def has_letters(s, pats):
    for c in pats:
        if c in s:
            return True
    return False

def has_pairs(s, n):
    i = 0
    np = 0
    while i < len(s)-1 and np < n:
        if s[i] == s[i+1]:
            np += 1
            i += 2
        else:
            i += 1
    return np == n

def valid_pass(p):
    if p == '':
        return False
    if not straight(p, 3):
        return False
    if has_letters(p, 'iol'):
        return False
    if not has_pairs(p, 2):
        return False
    return True

def next_pass(p):
    p1 = inc(p)
    while not valid_pass(p1):
        p1 = inc(p1)
    return p1

def main():
    assert('abcdffaa' == next_pass('abcdefgh'))
    assert('ghjaabcc' == next_pass('ghijklmn'))
    print next_pass('vzbxxyzz')

main()
