import re
import itertools

with open('day19.txt', 'r') as file:
  lines = [l.strip() for l in file.readlines()]

M = []

for l in lines:
  if "scanner" in l:
    scanner_id = int(re.search(r"\d+", l).group())
    M.append([])
  elif "," in l:
    M[scanner_id].append( tuple([int(i) for i in l.split(",")]) )

def sub_points(p1, p2):
  return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])

def normalize_points(point_set, ref_point):
  arr = []
  for point in point_set:
    arr.append(sub_points(point, ref_point))
  return arr

def translate_point(point, coord_permuation, signs):
  return (point[coord_permuation[0]] * signs[0], 
          point[coord_permuation[1]] * signs[1], 
          point[coord_permuation[2]] * signs[2])

def gen_permutations(scanner_points):
  ret = []
  for signs in itertools.product((1,-1),(1,-1),(1,-1)):
    for coord in itertools.permutations([0,1,2]):
      arr = set()
      for point in scanner_points:
        arr.add(translate_point(point, coord, signs))
      ret.append(arr)
  return ret

def overlap(s1, s2):
  for p1 in s1:
    for p2_permutation in gen_permutations(s2):
      for p2 in p2_permutation:
        diff = sub_points(p2, p1)
        s2_norm = normalize_points(p2_permutation, diff)

        intersect = set(s1).intersection(set(s2_norm))
        if len(intersect) >= 12:
          if diff not in scanners:
            scanners.append(diff)
          return s2_norm

P = set(M[0])
S = [0]
scanners = [(0,0,0)]

for s1 in range(len(M)):
  for s2 in range(len(M)):

    if s1 == s2:
      continue 
    
    if s2 in S:
      continue

    i = overlap(P, M[s2])
    if i:
      S.append(s2)
      P = P.union(i)

#1
print(len(P))

# 2
ret = 0
for s1 in scanners:
  for s2 in scanners:
    ret = max(ret, abs(s1[0]-s2[0]) + abs(s1[1]-s2[1]) + abs(s1[2]-s2[2]))
    
print(ret)