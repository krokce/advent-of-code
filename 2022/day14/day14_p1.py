import re
from collections import defaultdict

with open('day14.txt', 'r') as file:
    input = [l.strip() for l in file.readlines()]

I = (500,0)
C = defaultdict(int)
y_lim = 0
 
def fill_line(p1, p2):
    dx = 0
    dy = 0
    if p1[0] != p2[0]:
        dx = int((p2[0] - p1[0])/abs(p2[0] - p1[0]))
    if p1[1] != p2[1]:
        dy = int((p2[1] - p1[1])/abs(p2[1] - p1[1]))
    C[p1] = 1
    while p1 != p2:
        p1 = (p1[0]+dx, p1[1]+dy)
        C[p1] = 1

def cycle(p):
    for d in ((0, 1), (-1, 1), (1,1)):
        p_next = (p[0]+d[0], p[1]+d[1])
        if p_next[1] > y_lim:
            return I
        if C[p_next] > 0:
            if d == (1,1):                
                return p
        else:
            p = cycle(p_next)
            if p == I:
                return p
    return p

for scan_line in input:
    points = [int(i) for i in re.findall(r"\d+", scan_line)]
    line = []
    for i in range(0, len(points), 2):
        p = (points[i], points[i+1])
        y_lim = max(y_lim, p[1])
        line.append(p)
    for i in range(1,len(line),1):
        fill_line(line[i-1], line[i])

i = 0
while True:
    p = cycle(I)
    if p != I:
        C[p] = 2
        i += 1
    else:
        print(i)
        break