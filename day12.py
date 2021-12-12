with open('day12.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

P = {}
for l in input:
  p1,p2 = l.split("-")
  if p1 not in P:
    P[p1] = [p2]
  else: 
    P[p1].append(p2)
  if p2 not in P:
    P[p2] = [p1]
  else: 
    P[p2].append(p1)     

cnt1 = 0
def solve1(path, P, current_node):
  global cnt1
  path.append(current_node)
  if current_node == "end":
    cnt1 += 1
    return True
  else:
    for d in P[current_node]:
      if d.islower() and d not in path:
        solve1(path.copy(), P, d)
      elif d.isupper(): 
        solve1(path.copy(), P, d)
    return False

cnt2 = 0
def solve2(path, P, current_node, visited):
  global cnt2
  path.append(current_node)
  if current_node == "end":
    cnt2 += 1
    return True
  else:
    for d in P[current_node]:
      if d.islower() and d not in path:
        solve2(path.copy(), P, d, visited)
      elif d.islower() and d not in ["start", "end"] and path.count(d) < 2 and not visited:
        solve2(path.copy(), P, d, True)
      elif d.isupper():
        solve2(path.copy(), P, d, visited)
    return False

solve1([], P, "start")
print(cnt1)

solve2([], P, "start", False)
print(cnt2)