input = open('day06.txt', 'r').read()

l = list(map(int, input.split(",")))

f = [0 for i in range(9)]
for i in l:
  f[i] += 1

def new_day():
  ret=[]
  for i in range(len(f)-1):
    ret.append(f[i+1])
  ret[6] += f[0]
  ret.append(f[0])
  return ret

# 1
for day in range(80):
  f = new_day()
print(sum(i for i in f))

# 2
for day in range(256-80):
  f = new_day()
print(sum(i for i in f))