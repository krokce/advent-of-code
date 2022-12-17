from itertools import cycle

with open('day17.txt', 'r') as file:
    J = file.read().strip()

C = {}
R = [
        [(0,0), (1,0), (2,0), (3,0)],
        [(1,0), (0,1), (1,1), (2,1), (1,2)],
        [(0,0), (1,0), (2,0), (2,1), (2,2)],
        [(0,0), (0,1), (0,2), (0,3)],
        [(0,0), (1,0), (0,1), (1,1)]
    ] 

D = {
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, -1)
}

max_x = 7

def new_rock(id, dy):
    dx = 2
    return [(x+dx, y+dy) for x,y in R[id]]

def move_rock(rock, direction):
    dx, dy = D[direction]
    return [(x+dx, y+dy) for x,y in rock]

def is_rock_valid(rock):
    max_x = 7
    for x, y in rock:
        if x < 0 or y < 0 or x >= max_x or (x,y) in C:
            return False
    return True

def rest_rock(rock):
    for x, y in rock:
        C[(x,y)] = 1

def get_height():
    if len(C) == 0:
        return 0
    return max([y for _,y in C.keys()]) + 1

def draw_pit():
    y = get_height() + 2
    while y >= 0:
        line = ""
        for x in range(7):
            if (x,y) in C:
                line += "#"
            else: 
                line += "."
        print("|"+line+"|")
        y -= 1
    print("-"*(max_x+2))


jet_id = 0
rock_cnt = 0
height = 0
for rock_id in cycle(range(len(R))):
    height = get_height()
    rock_cnt += 1
    r = new_rock(rock_id, height+3)
    while True:
        # Jet push
        tmp_r = move_rock(r, J[jet_id])
        jet_id = jet_id + 1 if jet_id < len(J)-1 else 0
        if is_rock_valid(tmp_r):
            r = tmp_r
        # Fall down
        tmp_r = move_rock(r, "v")
        if is_rock_valid(tmp_r):
            r = tmp_r
        else:
            rest_rock(r)
            height = get_height()
            # draw_pit()
            break
    if rock_cnt == 2_022:
        break

# 1
print(height)