import itertools
from copy import deepcopy as dc
from functools import cmp_to_key
import time

start_time = time.time()

with open('day23.txt', 'r') as file:
  burrow = [[l.strip() for l in k] for k in file.readlines()]

A = {}
B = {}
for row in range(len(burrow)):
  for col in range(len(burrow[row])):
    if burrow[row][col] == ".":
      B[(row,col)] = [-1, (burrow[row][col-1] != "#", burrow[row][col+1] != "#", burrow[row-1][col] != "#", burrow[row+1][col] != "#")]
    elif burrow[row][col] in ("A", "B", "C", "D"):
      B[(row,col)] = [len(A), (burrow[row][col-1] != "#", burrow[row][col+1] != "#", burrow[row-1][col] != "#", burrow[row+1][col] != "#")]
      A[len(A)] = burrow[row][col]

AM = {i:0 for i in A.keys()}
directions = [(0,-1),(0,1),(-1,0),(1,0)] # left, right, up, down

final_rooms = {
  "A": 3,
  "B": 5,
  "C": 7,
  "D": 9
}

amphiboid_energy = {
  "A": 1,
  "B": 10,
  "C": 100,
  "D": 1000
}

def amphiboid_position(B, amphiboid_id):
  for k,v in B.items():
    if v[0] == amphiboid_id:
      return k

def valid_moves(B, AM, amphiboid_id, starting_position, energy):
  ret = []
  pos = amphiboid_position(B, amphiboid_id)
  
  for direction in list(itertools.compress(directions, (B[pos][1]))):
    next_step_pos = (pos[0]+direction[0], pos[1]+direction[1])
    next_step = B[next_step_pos]
    if next_step[0] == -1 and AM[amphiboid_id] < 2:
      if sum(next_step[1]) < 3:
        ret.append((pos[0]+direction[0], pos[1]+direction[1], energy + amphiboid_energy[A[amphiboid_id]]))
      B_copy = dc(B)
      AM_copy = dc(AM)
      B_copy[pos][0] = "#"
      B_copy[next_step_pos][0] = amphiboid_id
      new_pos = valid_moves(B_copy, AM_copy, amphiboid_id, starting_position, energy + amphiboid_energy[A[amphiboid_id]])
      ret += new_pos
  
  ret_ = []
  for i in range(len(ret)):

    # remove moves from corridor to corridor
    if starting_position[0] == 1 and ret[i][0] == 1:
      continue
    
    # remove moves from to the same room
    if starting_position[1] == ret[i][1]:
      continue

    # remove if second step is in corridor
    if AM[amphiboid_id] == 1 and ret[i][0] == 1:
      continue

    # step in room
    if ret[i][0] > 1:

      # remove if not in the right room
      if ret[i][1] != final_rooms[A[amphiboid_id]]:
        continue
      
      blocked_id_pos = (ret[i][0]+1, ret[i][1])
      # romove if blocks empty piece      
      if blocked_id_pos in B and B[blocked_id_pos][0] == -1:
        continue

      # remove if blocks other type
      if blocked_id_pos in B and B[blocked_id_pos][0] != -1 and blocked_id_pos[1] != final_rooms[A[(B[blocked_id_pos][0])]]:
        continue

      # if can be placed in room do it now and remove all other moves
      ret_.clear()
      ret_.append(ret[i])
      break

    ret_.append(ret[i])
  return ret_

def is_solved(B):
  for a_id, a_typ in A.items():
    pos = amphiboid_position(B, a_id)
    if pos[1] != final_rooms[A[a_id]]:
      return False
  return True

def amphiboids_not_parked(B):
  ret = []
  for pos, v in B.items():
    if v[0] != -1 and pos[1] != final_rooms[A[v[0]]]:
      ret.append(v[0])
    elif v[0] != -1:
      blocked_id_pos = (pos[0]+1, pos[1])
      if blocked_id_pos in B and B[blocked_id_pos][0] != -1 and blocked_id_pos[1] != final_rooms[A[(B[blocked_id_pos][0])]]:
        ret.append(v[0])
  return ret

def compare_moves(move1, move2):
  if move1[1][0] > move2[1][0]:
    return -1
  elif move2[1][0] > move1[1][0]:
    return 1
  elif move1[1][2] > move2[1][2]:
    return 1
  elif move2[1][2] > move1[1][2]:
    return -1
  else:
    return 0

S = {}
E = None

def solve(B, AM, energy):
  global E
  
  key = tuple((*k, v[0]) for k, v in B.items() if v[0] != -1)
  if key in S:
    return S[key]

  if is_solved(B):
    if not E or energy < E:
      print(energy)
      E = energy
    return True

  else:
    moves = []
    for a_id in amphiboids_not_parked(B):
      for m in sorted(valid_moves(B, AM, a_id, amphiboid_position(B, a_id), 0)):
        moves.append((a_id, m))

    for a_id, m in sorted(moves, key=cmp_to_key(compare_moves)):    
      pos = amphiboid_position(B, a_id)
      AM_copy = dc(AM)
      B_copy = dc(B)
      AM_copy[a_id] += 1
      B_copy[pos][0] = -1
      B_copy[(m[0], m[1])][0] = a_id
      if not solve(B_copy, AM_copy, energy + m[2]):
        S[tuple((*k, v[0]) for k, v in B_copy.items() if v[0] != -1)] = False
  
    return False

solve(B, AM, 0)
print(E)
print("--- %s seconds ---" % (time.time() - start_time))