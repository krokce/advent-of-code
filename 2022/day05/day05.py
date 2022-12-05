import re
with open('day05.txt', 'r') as file:
  input = [l for l in file.readlines()]
 
p1 = [[] for i in range(9)]
p2 = [[] for i in range(9)]
for l in input:
  s = re.findall(r"[a-zA-Z|#]+", l.replace("    ", "[#] "))
    
  if len(s) == 9:
    for i in range(9):
      if s[i] != '#':
        p1[i].insert(0, s[i])
        p2[i].insert(0, s[i])

  else:
    s = [int(i) for i in re.findall(r"\d+", l.strip())]
    if len(s) != 3:
      continue
    for m in range(s[0]):
      e = p1[s[1]-1].pop()
      p1[s[2]-1].append(e)
    
    p2[s[2]-1] = p2[s[2]-1] + p2[s[1]-1][-s[0]:]
    p2[s[1]-1] = p2[s[1]-1][0:-s[0]]

#1
print("".join([i[-1] for i in p1]))

#2
print("".join([i[-1] for i in p2]))