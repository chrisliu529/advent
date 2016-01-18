def s(n):
    return n*(n-1)/2 + 1

def d(n, m):
    return (m-1)*n + m*(m-1)/2

def s2(n, m):
    return s(n) + d(n, m)

def trans(c):
    return c * 252533 % 33554393

def code(n, m):
    times = s2(n, m)
    c = 20151125
    for i in range(times-1):
        c = trans(c)
    print "%s (%s, %s) = %s" % (times, n, m, c)
    return c

def main():
    assert 1 == s2(1, 1)
    assert 3 == s2(1, 2)
    assert 2 == s2(2, 1)
    assert 16 == s2(6, 1)
    assert 21 == s2(1, 6)

    assert 33511524 == code(1, 6)
    assert 27995004 == code(6, 6)
    assert 20151125 == code(1, 1)

    code(2978, 3083)

main()
