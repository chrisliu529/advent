def find_repeat_pair(s):
    for i in range(len(s)-1):
        pat = s[i:i+2]
        if s[i+2:].find(pat) >= 0:
            return True
    return False

def find_interval_single(s):
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            return True
    return False

def nice(s):
    if not find_repeat_pair(s):
        return False
    if not find_interval_single(s):
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
    assert nice('qjhvhtzxzqqjkmpb')
    assert not nice('uurcxstgmygtbstg')
    assert not nice('ieodomkazucvgmuy')

    print find_nice()

main()
