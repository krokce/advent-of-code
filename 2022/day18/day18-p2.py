import sys
from itertools import product
sys.setrecursionlimit(10000)

with open('day18.txt', 'r') as file:
    C = {(int(x),int(y),int(z)) for x,y,z in [l.split(",") for l in [l.strip() for l in file.readlines()]]}

max_X = max([x for x,_,_ in C])+1
min_X = min([x for x,_,_ in C])-1
max_Y = max([y for _,y,_ in C])+1
min_Y = min([y for _,y,_ in C])-1
max_Z = max([z for _,_,z in C])+1
min_Z = min([z for _,_,z in C])-1

seen = set()
def count_sides(x,y,z):
    ret = 0
    if x < min_X or x > max_X or y < min_Y or y > max_Y  or z < min_Z or z > max_Z:
        return 0
    for dx,dy,dz in [(x,y,z) for x,y,z in product((-1,0,1),(-1,0,1),(-1,0,1)) if abs(x)+abs(y)+abs(z) == 1]:
        next_cube = (x+dx, y+dy, z+dz)
        if next_cube in C:
            ret += 1
        elif next_cube not in seen:
            seen.add(next_cube)
            ret += count_sides(*next_cube)
    return ret 

#2
print(count_sides(min_X, min_Y, min_Z))