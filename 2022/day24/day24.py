import heapq

with open('day24.txt', 'r') as file:
    lines = [l.strip("\n") for l in file.readlines()]

D = {"v":(0,1), ">":(1,0), "^":(0,-1), "<":(-1,0)}
dimensions = (len(lines[0]), len(lines))

blizzard = []
wall = []
start = None
finish = None
for y, line in enumerate(lines):
    for x, val in enumerate(line):
        if val == "." and not start:
            start = (x,y)
        if val in ["<", ">", "^", "v"]:
            blizzard.append((val, (x,y)))
        elif val == "#":
            wall.append((x,y))
        if y == len(lines)-1 and val == "." and not finish:
            finish = (x,y)

def get_next_blizzard(blizzard):
    ret_b = []
    ret_m = set()
    for direction, (x, y) in blizzard:
        next_x, next_y = x + D[direction][0], y + D[direction][1]
        if (next_x, next_y) in wall:
            next_x =  x - D[direction][0]*(dimensions[0] - 3)
            next_y =  y - D[direction][1]*(dimensions[1] - 3)
        ret_b.append((direction, (next_x, next_y)))
        ret_m.add((x,y))
    return ret_b, ret_m

def solve(start, finish, blizzard): 
    Q = []
    heapq.heappush(Q, (0, start, blizzard))
    seen = set()
    BLZ = {}
    MAP = {}
    while True:
        time, position, blizzard = heapq.heappop(Q)

        if position == finish:
            return time, blizzard
        else:
            if time+1 not in BLZ:
                BLZ[time+1], MAP[time+1] = get_next_blizzard(blizzard)

            for d in [(0,1), (1,0), (0,-1), (-1,0), (0, 0)]:
                next_position = (position[0]+d[0], position[1]+d[1])

                if next_position in MAP[time+1] or next_position in wall or not 0 <= next_position[0] < dimensions[0] or not 0 <= next_position[1] < dimensions[1]:
                    continue

                if (time+1, next_position) in seen:
                    continue
                
                heapq.heappush(Q, (time+1, next_position, BLZ[time+1]))
                seen.add((time+1, next_position))

#1
t, blizzard = solve(start, finish, blizzard)
print(t-1)

#2
t2, blizzard = solve(finish, start, blizzard)
t3, blizzard = solve(start, finish, blizzard)
print(sum([t, t2, t3])-1)