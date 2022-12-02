with open('day14.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

R = {}
for l in input:
  if l != "" and "->" not in l:
    template = l.strip()
  elif "->" in l:
    str = l.split(" -> ")
    R[str[0]] = str[1].strip()

def add_letter(l, cnt):
  if l in letters:
    letters[l] += cnt
  else:
    letters[l] = cnt

letters = {}
for c in template:
  add_letter(c, 1)

P = {}
for c in range(len(template)-1):
  if template[c:c+2] in P:
    P[template[c:c+2]] += 1
  else:
    P[template[c:c+2]] = 1

def step():
  ret = {}
  for k, v in P.items():
    if k in R:
      add_letter(R[k], v)
      for new_pair in [k[0]+R[k], R[k]+k[1]]:
        if new_pair in ret:
          ret[new_pair] += v
        else:
          ret[new_pair] = v
    else:
      if k in ret:
        ret[k] += v
      else:
        ret[k] = v
  return ret      

# 1
for _ in range(10):
  P = step()
print(max(letters.values()) - min(letters.values()))

# 2
for _ in range(30):
  P = step()
print(max(letters.values()) - min(letters.values()))