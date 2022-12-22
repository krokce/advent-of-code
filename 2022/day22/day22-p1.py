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

def get_teleport_point(current_position, current_facing):
    # go back until hit none or blank
    x, y = current_position
    dx, dy = F[current_facing]
    while True:
        x, y = x - dx, y - dy
        if (x, y) not in M or M[(x, y)] == " ":
            break
    return (x + dx, y + dy)

def make_step(current_facing, current_position):
    x, y = current_position
    dx, dy = F[current_facing]
    next_x, next_y = x + dx, y + dy
    if (next_x, next_y) not in M or M[(next_x, next_y)] == " ":
        (next_x, next_y) = get_teleport_point((next_x, next_y), current_facing)
    if M[(next_x, next_y)] == "#":
        return current_position
    else:
        return (next_x, next_y)

for steps, turn_direction in path:
    for s in range(int(steps)):
        next_position = make_step(current_facing, current_position)
        if next_position == current_position:
            break
        current_position = next_position
    
    if turn_direction != "S":
        current_facing = make_turn(current_facing, turn_direction)
    else:
        pass

#1
print(1000 * current_position[1] + 4 * current_position[0] + current_facing)