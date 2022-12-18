from itertools import product

with open('day18.txt', 'r') as file:
    C = {(int(x),int(y),int(z)) for x,y,z in [l.split(",") for l in [l.strip() for l in file.readlines()]]}

def count_exposed(c):
    x,y,z = c
    ret = 0
    for dx,dy,dz in [(x,y,z) for x,y,z in product((-1,0,1),(-1,0,1),(-1,0,1)) if abs(x)+abs(y)+abs(z) == 1]:
        if (x+dx, y+dy, z+dz) not in C:
            ret += 1
    return ret

#1
print(sum([count_exposed(c) for c in C]))