from z3 import *

with open("day24.txt", "r") as file:
    lines = [
        list(tuple(map(int, k.split(", "))) for k in l.strip().split("@"))
        for l in file.readlines()
    ]

x, y, z, vx, vy, vz = Ints("x y z vx vy vz")
t = [Int(f"t{i}") for i in range(len(lines))]

s = Solver()
for hailstone_id, ((x1, y1, z1), (vx1, vy1, vz1)) in enumerate(lines):
    s.add(x + vx * t[hailstone_id] == x1 + vx1 * t[hailstone_id])
    s.add(y + vy * t[hailstone_id] == y1 + vy1 * t[hailstone_id])
    s.add(z + vz * t[hailstone_id] == z1 + vz1 * t[hailstone_id])

s.check()
m = s.model()
print(m[x].as_long() + m[y].as_long() + m[z].as_long())