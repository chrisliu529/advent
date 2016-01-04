def do_trans(s):
    i = 0
    prev = s[i]
    ns = ''
    cnt = 0
    ch = prev
    while i < len(s):
        while i < len(s) and ch == prev:
            cnt += 1
            i += 1
            if i < len(s):
                ch = s[i]            
        ns += str(cnt) + prev
        if i == len(s):
            return ns
        prev = ch
        cnt = 0
    return ns

def trans(s, n):
    for i in range(n):
        s = do_trans(s)
    return s

def main():
    print len(trans('3113322113', 50))

main()
