import itertools

def neighbors_val(tree, p1, p2):
    return tree['%s,%s' % (p1, p2)] + tree['%s,%s' % (p2, p1)]

def happy_val(tree, seats):
    s = 0
    for i in range(len(seats) - 1):
        s += neighbors_val(tree, seats[i], seats[i+1])
    s += neighbors_val(tree, seats[0], seats[-1])
    return s

def happiest(tree, friends):
    h = -10000000
    for seats in itertools.permutations(friends):
        v = happy_val(tree, seats)
        if v > h:
            h = v
    return h

def parse_line(line):
    fields = line.split()
    p1 = fields[0]
    p2 = fields[10][:-1]
    v = int(fields[3])
    if fields[2] == 'lose':
        v = -v
    return p1, p2, v

def optimal_seats(f):
    s = file(f).read()
    happy_tree = {}
    friends = set()
    for line in s.split('\n'):
        if line == '':
            continue
        p1, p2, v = parse_line(line)
        friends.add(p1)
        happy_tree['%s,%s' % (p1, p2)] = v

    friends.add('You')
    for f in friends:
        happy_tree['You,%s' % f] = 0
        happy_tree['%s,You' % f] = 0

    return happiest(happy_tree, list(friends))

def main():
    print optimal_seats('input13')

main()
