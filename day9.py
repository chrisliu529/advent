import sys
import re

class SantaMap(object):
    def __init__(self):
        self.edges = {}
        self.result = {}

    def insert_edge_raw(self, start, end, weight):
        try:
            self.edges[start][end] = weight
        except KeyError:
            self.edges[start] = {end: weight}
        
    def insert_edge(self, edge):
        start = edge.start
        end = edge.end
        weight = edge.weight
        self.insert_edge_raw(start, end, weight)
        self.insert_edge_raw(end, start, weight)

    def num_cities(self):
        return len(self.edges.keys())

    def check_path(self, city, v, visited):
        candidates = self.edges[city]
        for k in candidates.keys():
            if k in visited:
                continue
            visited.append(k)
            v += candidates[k]
            if len(visited) == self.num_cities():
                self.result['->'.join(visited)] = v
            self.check_path(k, v, visited)
            v -= candidates[k]
            visited.pop()
        
    def shortest_path(self):
        visited = []
        for k in self.edges.keys():
            visited.append(k)
            self.check_path(k, 0, visited)
            visited = []

        min_path_v = 999999
        min_path = ''
        for k in self.result:
            path_v = self.result[k]
            if path_v < min_path_v:
                min_path_v = path_v
                min_path = k
        print min_path
        return min_path_v

class Edge(object):
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

def parse_edge(line):
    m = re.match(r'(\w+) to (\w+) = (\w+)', line)
    return Edge(m.group(1), m.group(2), int(m.group(3)))

def main():
    santa_map = SantaMap()
    f = file(sys.argv[1])
    lines = f.read().split('\n')
    for line in lines:
        if line == '':
            continue
        print line
        edge = parse_edge(line)
        santa_map.insert_edge(edge)
    print santa_map.shortest_path()

main()
