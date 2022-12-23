import re
from collections import deque
with open('day23.txt', 'r') as file:
    lines = [l.strip("\n") for l in file.readlines()]

M = set()
for y, l in enumerate(lines):
    for x, v in enumerate(l):
        if v == "#":
            M.add((x,y))

D = {"N":(0,-1), "NE": (1,-1), "NW": (-1,-1),"S":(0,1), "SE": (1,1), "SW": (-1,1),"E":(1,0),"W":(-1,0)}
check_order = deque([("N","NE","NW"), ("S","SE","SW"), ("W","NW","SW"), ("E","NE","SE")])
move = deque(["N", "S", "W", "E"])

def next_proposed_move(position, check_order):
    x,y = position

    # stay in place if no one is around
    if sum([1 for dx,dy in D.values() if (x+dx, y+dy) in M]) == 0:
        return position

    # follow the check_order to propose a move 
    for move_id, check in enumerate(check_order):
        move_to_dx, move_to_dy = D[move[move_id]]
        
        is_move = True
        for c in check:
            dx, dy = D[c]
            if (x+dx, y+dy) in M:
                is_move = False
                break

        if is_move:
            return (x+move_to_dx, y+move_to_dy)
    return position

def step():
    # get proposed moves
    unique_moves = set()
    proposed_moves = {}
    for position in M:
        proposed_move = next_proposed_move(position, check_order)
        if position != proposed_move:
            proposed_moves[position] = proposed_move
            unique_moves = unique_moves ^ {proposed_move}

    # make moves
    for from_position, to_position in proposed_moves.items():
        if to_position in unique_moves:
            M.add(to_position)
            M.remove(from_position)
    
    # shift priorities
    check_order.append(check_order.popleft())
    move.append(move.popleft())

    # return number of moves made
    return len(unique_moves)

def count_empty_ground():
    minx = min([x for x, y in M])
    maxx = max([x for x, y in M])
    miny = min([y for x, y in M])
    maxy = max([y for x, y in M])
    return (maxx-minx+1)*(maxy-miny+1)-len(M)

round = 0
while True:
    round += 1

    # 2
    if step() == 0:
        print(round)
        break

    # 1
    if round == 10:
        print(count_empty_ground())