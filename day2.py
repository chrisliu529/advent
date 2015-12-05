def warp_area(sizes):
    l = sizes[0]
    w = sizes[1]
    h = sizes[2]
    area = 2*(l*w + w*h + l*h)
    return area + l*w

def ribbon_length(sizes):
    l = sizes[0]
    w = sizes[1]
    h = sizes[2]
    return 2*(l+w) + l*w*h
    
def calc(line):
    sizes = [int(s) for s in line.split('x') if s != '']
    if len(sizes) < 3:
        return 0
    sizes.sort()
    return ribbon_length(sizes)

def main():
    f = file('input2')
    lines = f.read().split('\n')
    result = sum([ calc(l) for l in lines])
    print result
    assert ribbon_length([1, 1, 10]) == 14

main()
