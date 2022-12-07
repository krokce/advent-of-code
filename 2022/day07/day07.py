with open('day07.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

D = {}

def cd(cur_dir, to_dir):
  dirs = cur_dir.split("/")
  if to_dir == "/":
    return "/root"
  elif to_dir == "..":
    return "/".join(dirs[0:-1])
  else:
    return "/".join(dirs+[to_dir])

def add_file(cur_dir, file_size):
  s_cur_dir = "" 
  for s in cur_dir.split("/"):
    if s == "":
      continue
    s_cur_dir = s_cur_dir + "/" + s 
    if s_cur_dir not in D:
      D[s_cur_dir] = file_size
    else:
      D[s_cur_dir] += file_size

cur_dir = ''
for i in input:
  c = i.split(" ")
  if c[1] == 'cd':
    cur_dir = cd(cur_dir, c[2])
  if c[0] not in ["$", "dir"]:
    add_file(cur_dir, int(c[0]))

#1
print(sum(d for d in D.values() if d <= 100000))

#2
print(min(d for d in D.values() if 70000000 - D["/root"] + d > 30000000))
