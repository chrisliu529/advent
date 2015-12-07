def vowels(s):
    return [c for c in s if c in 'aeiou']

def appear_twice(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False

def include_str(s, arr):
    for p in arr:
        if s.find(p) >= 0:
            return True
    return False

def nice(s):
    v = vowels(s)
    if len(v) < 3:
        return False
    if not appear_twice(s):
        return False
    if include_str(s, ['ab', 'cd', 'pq', 'xy']):
        return False
    return True

def find_nice():
    f = file('input5')
    lines = f.read().split('\n')
    cnt = 0
    for l in lines:
        if nice(l):
            cnt += 1
    return cnt    

def main():
    assert nice('ugknbfddgicrmopn')
    assert nice('aaa')
    assert not nice('jchzalrnumimnmhp')
    assert not nice('haegwjzuvuyypxyu')
    assert not nice('dvszwmarrgswjxmb')

    print find_nice()

main()
