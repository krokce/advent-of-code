with open('day06.txt', 'r') as file:
  lines = [l.strip().split(")") for l in file.readlines()]

M = {y:x for x,y in lines}

def orbits(obj, orbit_set):
  if obj not in M:
    return orbit_set
  else: 
    orbit_set.add(obj)
    return orbits(M[obj], orbit_set)

# 1
print(sum(len(orbits(o, set())) for o in M.keys()))

# 2
print(len(orbits("YOU", set()) ^ orbits("SAN", set())) - 2)