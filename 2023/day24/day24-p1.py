with open("day24.txt", "r") as file:
    lines = [
        list(tuple(map(int, k.split(", "))) for k in l.strip().split("@"))
        for l in file.readlines()
    ]

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
    return (x, y)

test_area = ((200000000000000, 400000000000000), (200000000000000,400000000000000))

paths = []
for ((x1, y1, z1), (vx, vy, vz)) in lines:
    p1 = (x1, y1)
    p2 = (x1+vx, y1+vy)
    paths.append((p1,p2))

ret = 0
for i in range(len(paths)):
    for j in range(i+1, len(paths)):
        cross = get_intersection_point(paths[i][0], paths[i][1], paths[j][0], paths[j][1])
        if cross and test_area[0][0] < cross[0] < test_area[0][1] and test_area[1][0] < cross[1] < test_area[1][1]:
            time_a = (cross[0] - paths[i][0][0])/lines[i][1][0]
            time_b = (cross[0] - paths[j][0][0])/lines[j][1][0]
            if time_a > 0 and time_b > 0:
                ret += 1
print(ret)