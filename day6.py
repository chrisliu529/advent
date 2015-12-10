import sys

class Command(object):
    def __init__(self, action, start_pos, end_pos):
        self.action = action
        self.start_pos = start_pos
        self.end_pos = end_pos

def parse_pos(cord_str):
    l = cord_str.split(',')
    return (int(l[0]), int(l[1]))

def parse_command(line):
    words = line.split(' ')

    if words[0] == 'turn':
        if words[1] == 'on':
            action = 'on'
        else:
            action = 'off'
        start_pos = parse_pos(words[2])
        end_pos = parse_pos(words[4])
    else:
        action = 'toggle'
        start_pos = parse_pos(words[1])
        end_pos = parse_pos(words[3])

    return Command(action, start_pos, end_pos)

def turn_on(start, end, lights):
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            lights[x][y] = 1

def turn_off(start, end, lights):
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            lights[x][y] = 0

def toggle(start, end, lights):
    for x in range(start[0], end[0]+1):
        for y in range(start[1], end[1]+1):
            if lights[x][y] == 0:
                lights[x][y] = 1
            else:
                lights[x][y] = 0

def apply_command(cmd, lights):
    if cmd.action == 'on':
        turn_on(cmd.start_pos, cmd.end_pos, lights)
    elif cmd.action == 'off':
        turn_off(cmd.start_pos, cmd.end_pos, lights)
    else:
        toggle(cmd.start_pos, cmd.end_pos, lights)

def count(lights):
    cnt = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            cnt += lights[x][y]
    return cnt

def main():
    lights = [[0 for x in range(1000)] for x in range(1000)]
    f = file(sys.argv[1])
    lines = f.read().split('\n')
    for line in lines:
        cmd = parse_command(line)
        apply_command(cmd, lights)
    print count(lights)

main()
