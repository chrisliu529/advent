class Deer(object):
    def __init__(self, name, speed, run_time, rest_time):
        self.name = name
        self.speed = speed
        self.run_time = run_time
        self.rest_time = rest_time

    def run(self, time):
        t = self.run_time + self.rest_time
        turns = time / t
        remain = time % t
        if remain > self.run_time:
            remain = self.run_time
        return (turns*self.run_time + remain)*self.speed

def parse_deer(line):
    l = line.split()
    return Deer(l[0], int(l[3]), int(l[6]), int(l[13]))

def read_deers(path):
    f = file(path)
    lines = f.read().split('\n')
    deers = []
    for line in lines:
        if line == '':
            continue
        deer = parse_deer(line)
        deers.append(deer)
    return deers

def win_deer(path, time):
    return max([x.run(time) for x in read_deers(path)])

def win_deer2(path, time):
    deers = read_deers(path)
    furthest = 0
    points = {}
    for i in range(time):
        leaders = []
        for x in deers:
            ran_distance = x.run(i+1)
            if ran_distance > furthest:
                furthest = ran_distance
                leaders = [x.name]
            elif ran_distance == furthest:
                leaders.append(x.name)
        for leader in leaders:
            try:
                points[leader] += 1
            except KeyError:
                points[leader] = 1
    print points
    return max(points.values())

def main():
    assert 1120 == win_deer('input14a', 1000)
    assert 689 == win_deer2('input14a', 1000)
    print win_deer('input14', 2503)
    print win_deer2('input14', 2503)

main()
