import math

with open('day09.txt', 'r') as file:
  input = [l.strip().split(" ") for l in file.readlines()]

D = {"U":(0, 1), "D":(0, -1), "R":(1, 0), "L":(-1, 0)}

def get_next_position(rope, node_id):
  head = rope[node_id-1]
  tail = rope[node_id]
  if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
    dx = (head[0]-tail[0])/2
    dx = math.copysign(math.ceil(abs(dx)), dx)
    dy = (head[1]-tail[1])/2
    dy = math.copysign(math.ceil(abs(dy)), dy)
    return (tail[0]+dx, tail[1]+dy)
  else:
    return tail

def solve(rope_length):
  rope = {i:(0,0) for i in range(rope_length)}
  visited = set()
  for direction, steps in input:
    for step in range(int(steps)):      
      rope[0] = (rope[0][0] + D[direction][0], rope[0][1] + D[direction][1])
      for node in range(1, len(rope)):
        rope[node] = get_next_position(rope, node)
      visited.add(rope[rope_length-1])
  return len(visited)

#1
print(solve(2))

#2
print(solve(10))