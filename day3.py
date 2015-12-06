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
    visited[santa.key()] = True
    for c in s:
        if c == '^':
            santa.up()
        elif c == '<':
            santa.left()
        elif c == '>':
            santa.right()
        elif c == 'v':
            santa.down()
        else:
            assert(False)
        visited[santa.key()] = True
    houses = visited.keys()
    return len(visited.keys())

def main():
    f = file('input3')
    s = f.read()
    assert calc('>') == 2
    assert calc('^>v<') == 4
    assert calc('^v^v^v^v^v') == 2

    print calc(s)
    
main()
