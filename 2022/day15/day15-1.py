import re
with open('day15.txt', 'r') as file:
    input = [l.strip() for l in file.readlines()]

S = []
B = []
D = []

def distance(a,b):
    return abs(a[0]-b[0]) +  abs(a[1]-b[1])

for scan_line in input:
    sx,sy,bx,by = [int(i) for i in re.findall(r"[\d|-]+", scan_line)]
    S.append((sx,sy))
    B.append((bx,by))
    D.append(distance(S[-1], B[-1]))

def solve(y):
    ret = set()
    for scanner_id in range(len(S)):
        sx, sy = S[scanner_id]
        d = D[scanner_id]
        for dy in [sy+d, sy-d]:
            if sy <= y <= dy or sy >= y >= dy:
                delta = abs(dy - y)
                for x in range(-delta+sx, delta+sx+1):
                    if (x, y) not in B:
                        ret.add(x)
    return len(ret)

#1
print(solve(10))