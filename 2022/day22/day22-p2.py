import re
with open('day22.txt', 'r') as file:
    lines = [l.strip("\n") for l in file.readlines()]

# 0 for right (>)
# 1 for down (v) 
# 2 for left (<) 
# 3 for up (^)

F = {0: (1,0), 1: (0,1), 2: (-1, 0), 3: (0, -1)}

D = {"R":1, "L":-1}
M = {}
current_facing = 0
current_position = None

for y, line in enumerate(lines):
    if line == '':
        path = re.findall("(\d+)([L|R]{1})", lines[y+1])
        path.append( (*re.findall("(\d+)$", lines[y+1]), "S") )
        break
    for x, value in enumerate(line):
        M[x+1, y+1] = value
        if value == "." and current_position is None:
            current_position = (x+1, y+1)

def make_turn(current_facing, direction):
    return (current_facing+D[direction])%len(F)

# Cube warping / teleport rules 
# (x,y,facing) => (next_x, next_y, next_facing)
T = {
    (tuple(range(51,101)), tuple([1]), 3): (lambda x,y: (1, x+100), 0), #1
    (tuple([1]), tuple(range(151,201)), 2): (lambda x,y: (y-100, 1), 1), #2
    (tuple(range(101,151)), tuple([1]), 3): (lambda x,y: (x-100, 200), 3), #3
    (tuple(range(1,51)), tuple([200]), 1): (lambda x,y: (x+100, 1), 1), #4
    (tuple([51]), tuple(range(1,51)), 2): (lambda x,y: (1, 151-y), 0), #5
    (tuple([1]), tuple(range(101,151)), 2): (lambda x,y: (51, 151-y), 0), #6
    (tuple([150]), tuple(range(1,51)), 0): (lambda x,y: (100, 151-y), 2), #7
    (tuple([100]), tuple(range(101,151)), 0): (lambda x,y: (150, 151-y), 2), #8
    (tuple(range(101,151)), tuple([50]), 1): (lambda x,y: (100, x-50), 2), #9
    (tuple([100]), tuple(range(51,101)), 0): (lambda x,y: (y+50, 50), 3), #10
    (tuple([51]), tuple(range(51,101)), 2): (lambda x,y: (y-50, 101), 1), #11
    (tuple(range(1,51)), tuple([101]), 3): (lambda x,y: (51, x+50), 0), #12
    (tuple(range(51,101)), tuple([150]), 1): (lambda x,y: (50, x+100), 2), #13
    (tuple([50]), tuple(range(151,201)), 0): (lambda x,y: (y-100, 150), 3), #14
}

def get_teleport_point(current_position, current_facing):
    x, y = current_position
    next_x, next_y = (0, 0)
    for tx, ty, cf in T:
        if x in tx and y in ty and cf == current_facing:
            next_x, next_y = T[(tx,ty,current_facing)][0](x, y)
            next_facing = T[(tx,ty,current_facing)][1]
            break
        assert current_position != (0,0) 
    return next_x, next_y, next_facing

def make_step(current_facing, current_position):
    x, y = current_position
    dx, dy = F[current_facing]
    next_x, next_y = x + dx, y + dy
    next_facing = current_facing
    if (next_x, next_y) not in M or M[(next_x, next_y)] == " ":
        next_x, next_y, next_facing = get_teleport_point((x, y), current_facing)

    if M[(next_x, next_y)] == "#":
        return x, y, current_facing
    else:
        return next_x, next_y, next_facing

for steps, turn_direction in path:
    for s in range(int(steps)):
        next_x, next_y, next_facing = make_step(current_facing, current_position)
        if (next_x, next_y) == current_position:
            break
        current_position = (next_x, next_y)
        current_facing = next_facing
    
    if turn_direction != "S":
        current_facing = make_turn(current_facing, turn_direction)
    else:
        pass

assert get_teleport_point((60,1),3) == (1, 160, 0) #1
assert get_teleport_point((1,160),2) == (60, 1, 1) #2
assert get_teleport_point((110,1),3) == (10, 200, 3) #3
assert get_teleport_point((10,200),1) == (110, 1, 1) #4
assert get_teleport_point((51,1),2) == (1, 150, 0) #5
assert get_teleport_point((1,101),2) == (51, 50, 0) #6
assert get_teleport_point((150,1),0) == (100, 150, 2) #7
assert get_teleport_point((100,101),0) == (150, 50, 2) #8
assert get_teleport_point((110,50),1) == (100, 60, 2) #9
assert get_teleport_point((100,60),0) == (110, 50, 3) #10
assert get_teleport_point((51,60),2) == (10, 101, 1) #11
assert get_teleport_point((10,101),3) == (51, 60, 0) #12
assert get_teleport_point((51,150),1) == (50, 151, 2) #13
assert get_teleport_point((50,151),0) == (51, 150, 3) #14

#2
print(1000 * current_position[1] + 4 * current_position[0] + current_facing)