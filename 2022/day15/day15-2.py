import re
from itertools import combinations

with open('day15.txt', 'r') as file:
    input = [l.strip() for l in file.readlines()]

S = []
B = []
D = []

def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

for scan_line in input:
    sx,sy,bx,by = [int(i) for i in re.findall(r"[\d|-]+", scan_line)]
    S.append((sx,sy))
    B.append((bx,by))
    D.append(distance(S[-1], B[-1]))

def is_scanned(p):
    for scanner_id in range(len(S)):
        if distance(p, S[scanner_id]) <= D[scanner_id]:
            return True
    return False

def get_intersection_point(p1, p2, p3, p4):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    if ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)) == 0:
        return None
    x = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    y = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    return (int(x), int(y))

def get_scanner_borders(scanner_id):
    x, y = S[scanner_id]
    d = D[scanner_id]
    p = [(x-d,y), (x,y+d), (x+d,y), (x,y-d)]
    return(((p[0], p[1]), (p[1], p[2]), (p[2], p[3]), (p[3], p[0])))

def solve(min_coord, max_coord):

    intersections = set()
    for scanner_id1, scanner_id2 in combinations(range(len(S)), 2):
        for line1 in get_scanner_borders(scanner_id1):
            for line2 in get_scanner_borders(scanner_id2):
                intersection = get_intersection_point(*line1, *line2)
                if intersection is not None:
                    intersections.add(intersection)

    for i in intersections:
        for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
            x = i[0]+dx
            y = i[1]+dy
            if not is_scanned((x, y)) and min_coord <= x <= max_coord and min_coord <= y <= max_coord:
                return x*4000000 + y

#2
print(solve(0, 4000000))