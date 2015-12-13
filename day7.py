import sys

class Gate(object):
    def __init__(self, operator, operands, out):
        self.operator = operator
        self.operands = operands
        self.out = out

def to_int(wire):
    try:
        i = int(wire)
    except ValueError:
        return None, False
    return i, True

def calc2(gates, wire):
    i, is_int = to_int(wire)
    if is_int:
        return i
    gate = gates[wire]
    op = gate.operator
    operands = gate.operands
    if op == '':
        assert len(operands) == 1
        return calc(gates, operands[0])
    if op == 'NOT':
        assert len(operands) == 1
        x = calc(gates, operands[0])
        return ~x + 65536
    if op == 'AND':
        assert len(operands) == 2
        return calc(gates, operands[0]) & calc(gates, operands[1])
    if op == 'OR':
        assert len(operands) == 2
        return calc(gates, operands[0]) | calc(gates, operands[1])
    if op == 'RSHIFT':
        assert len(operands) == 2
        return calc(gates, operands[0]) >> calc(gates, operands[1])
    if op == 'LSHIFT':
        assert len(operands) == 2
        return calc(gates, operands[0]) << calc(gates, operands[1])

    print op
    assert(False)

visited = {}

def calc(gates, wire):
    try:
        return visited[wire]
    except KeyError:
        res = calc2(gates, wire)
        visited[wire] = res
        return res

def parse_gate(line):
    parts = line.split('->')
    out = parts[1].strip()
    in_objs = parts[0].strip().split(' ')
    if len(in_objs) == 2:
        return Gate(in_objs[0], [in_objs[1]], out)
    if len(in_objs) == 3:
        return Gate(in_objs[1], [in_objs[0], in_objs[2]], out)
    if len(in_objs) == 1:
        return Gate('', [in_objs[0]], out)

def main():
    gates = {}
    f = file(sys.argv[1])
    lines = f.read().split('\n')
    for line in lines:
        if line == '':
            continue
        gate = parse_gate(line)
        gates[gate.out] = gate
    print calc(gates, 'a')

main()
