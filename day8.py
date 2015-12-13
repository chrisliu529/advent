import sys

def cnt_extra_chars(line):
    cnt = 0
    if line[0] == '"':
        cnt += 2
    if line[-1] == '"':
        cnt += 2
    for c in line[1:-1]:
        if c == '"':
            cnt += 1
        elif c == '\\':
            cnt += 1
    return cnt

def main():
    assert cnt_extra_chars('""') == 4
    assert cnt_extra_chars('"abc"') == 4
    assert cnt_extra_chars('"aaa\\"aaa"') == 6
    assert cnt_extra_chars('"\\x27"') == 5
    f = file(sys.argv[1])
    lines = f.read().split('\n')
    cnt0 = 0
    for line in lines:
        if line == '':
            continue
        print line, len(line)
        cnt0 += cnt_extra_chars(line)
    print cnt0

main()
