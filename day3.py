lines = open('day3.txt', 'r').readlines()

sample = "101010100101"
# sample = "01010"

ret = [[0, 0] for i in range(len(sample))]

# 1
for l in lines:
  l = l.strip()
  for d in range(len(l)):
    
    if int(l[d]) == 0:
      ret[d][0] += 1
    else:
      ret[d][1] += 1

g = ""
e = ""
for i in ret:
  if i[0] > i[1]:
    g = g + '0'
    e = e + '1'
  else:
    g = g + '1'
    e = e + '0'

print(int(g, 2) * int(e, 2) )

# 2
o_arr = []
c_arr = []
lines_o = lines.copy()
lines_c = lines.copy()

for d in range(len(sample)):
  cnt0 = 0
  cnt1 = 0
  lines0 = []
  lines1 = []
  for l in lines_o:
    l = l.strip()

    if int(l[d]) == 0:
      cnt0 += 1
      lines0.append(l)
    else:
      cnt1 += 1
      lines1.append(l)

  if cnt1 >= cnt0:
    lines_o = lines1
  else:
    lines_o = lines0

  if len(lines_o) == 1:
    break

for d in range(len(sample)):
  cnt0 = 0
  cnt1 = 0
  lines0 = []
  lines1 = []
  for l in lines_c:
    l = l.strip()

    if int(l[d]) == 0:
      cnt0 += 1
      lines0.append(l)
    else:
      cnt1 += 1
      lines1.append(l)

  if cnt0 <= cnt1:
    lines_c = lines0
  else:
    lines_c = lines1

  if len(lines_c) == 1:
    break

print(int(lines_c[0], 2) * int(lines_o[0], 2))