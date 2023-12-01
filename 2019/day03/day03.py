with open('day03.txt', 'r') as file:
  input = file.readlines()

lines = {}
position = {}
distances = {}
directions = {"U":(0, 1),"D":(0, -1),"L":(-1, 0),"R":(1, 0)}

def get_line(n, step):
  pos = (0,0) if len(position[n]) == 0 else position[n][-1]
  d = step[0]
  n = int(step[1:])
  return (pos, (pos[0]+directions[d][0]*n, pos[1]+directions[d][1]*n)), abs(directions[d][0]*n) + abs(directions[d][1]*n)

for n, l in enumerate(input):
  if n not in lines:
    lines[n] = []
    position[n] = []
    distances[n] = []

  for step in l.strip().split(","):
    line, distance = get_line(n, step)
    lines[n].append(line)
    position[n].append(line[1])
    distances[n].append(distance)

def line_direction(line):
  if line[0][0] == line[1][0]:
    return "V"
  elif line[0][1] == line[1][1]:
    return "H"
  else:
    print("Error")
    return None

def line_intersection(line1, line2):
  d1 = line_direction(line1)
  d2 = line_direction(line2)
  if d1 == "H": 
    h = line1
    v = line2
  else:
    h = line2
    v = line1

  if d1 != d2 and min(h[0][0], h[1][0]) < v[0][0] < max(h[0][0], h[1][0]) and min(v[0][1], v[1][1]) < h[0][1] < max(v[0][1], v[1][1]):
    return True, (v[0][0], h[0][1])
  else:
    return False, (None, None)

intersections = []
intersect_lines = []

for i, line1 in enumerate(lines[0]):
  for j, line2 in enumerate(lines[1]):
    is_intersect, intersect_point = line_intersection(line1, line2)
    if is_intersect:
      intersections.append(intersect_point)
      intersect_lines.append((i, j))

def get_distance(l1, l2):
  pl1 = position[0][l1-1]
  pl2 = position[1][l2-1]
  _, i = line_intersection(lines[0][l1], lines[1][l2])
  return sum(distances[0][0:l1]) + sum(distances[1][0:l2]) + abs(i[0]-pl1[0]) + abs(i[0]-pl2[0]) + abs(i[1]-pl1[1]) + abs(i[1]-pl2[1])

# 1
m = None
for i in intersections:
  if not m or abs(i[0]) + abs(i[1]) < m:
    m = abs(i[0]) + abs(i[1])
print(m)

# 2
d = None
for i in intersect_lines:
  tmp = get_distance(i[0], i[1])
  if not d or  tmp < d:
    d = tmp

print(d)