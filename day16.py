def parse_sue(line):
    #Sue 1: children: 1, cars: 8, vizslas: 7
    l = line.split()
    d = {'id': int(l[1][:-1])}
    d[l[2][:-1]] = int(l[3][:-1])
    d[l[4][:-1]] = int(l[5][:-1])
    d[l[6][:-1]] = int(l[7])
    return d

def parse_sues(path):
    f = file(path)
    lines = f.read().split('\n')
    sues = []
    for line in lines:
        if line == '':
            continue
        sue = parse_sue(line)
        sues.append(sue)
    return sues

def matched(aunt, pat):
    for k in aunt.keys():
        if k != 'id' and aunt[k] != pat[k]:
            return False
    return True

def find_aunt(path):
    sues = parse_sues(path)
    pat = {'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
            }
    for s in sues:
        if matched(s, pat):
            print s['id']

def main():
    find_aunt('input16')

main()
