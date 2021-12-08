with open('day8.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

N = {3:7, 7:8, 2:1, 4:4}
ret = 0

def diff(a, b):
  return sum(1 for i in a if i not in b)

for l in input:
  signal, output = l.split(" | ")
  D={}
  V={}

  for digit in signal.split(" "):
    d = list(digit)
    d.sort()
    v = "".join(d)
    if len(digit) in N:
      D[v] = N[len(digit)]
      V[D[v]] = v
    else:
      D[v] = -1

  for k, v in D.items():
    if len(k) == 5 and diff(k, V[1]) == 3:
      D[k] = 3
    elif len(k) == 5 and diff(k, V[4]) == 3:
      D[k] = 2
    elif len(k) == 5 and diff(k, V[4]) == 2:
      D[k] = 5
    elif len(k) == 6 and diff(k, V[4]) == 2 and diff(k, V[7]) == 3:
      D[k] = 9
    elif len(k) == 6 and diff(k, V[4]) == 3 and diff(k, V[7]) == 4:
      D[k] = 6
    elif len(k) == 6 and diff(k, V[4]) == 3 and diff(k, V[7]) == 3:
      D[k] = 0

  n = ""
  for digit in output.split(" "):
    d = list(digit)
    d.sort()
    d = "".join(d)
    n = n + str(D[d])
  ret += int(n)

print(ret)