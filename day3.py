class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def key(self):
        return '(%s,%s)' % (self.x, self.y)

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1

def calc(s):
    x = 0
    y = 0
    visited = {}
    santa = Location(0, 0)
    robot = Location(0, 0)
    visited[santa.key()] = True
    cnt = 0
    for c in s:
        obj = santa
        if cnt % 2 == 1:
            obj = robot
        if c == '^':
            obj.up()
        elif c == '<':
            obj.left()
        elif c == '>':
            obj.right()
        elif c == 'v':
            obj.down()
        else:
            assert(False)
        visited[obj.key()] = True
        cnt += 1
    houses = visited.keys()
    return len(visited.keys())

def main():
    f = file('input3')
    s = f.read()
    assert calc('^v') == 3
    assert calc('^>v<') == 3
    assert calc('^v^v^v^v^v') == 11

    print calc(s)
    
main()
