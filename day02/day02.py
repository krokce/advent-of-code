lines = open('day02.txt', 'r').readlines()

# 1
position = 0
depth = 0

for l in lines:
  direction, value = l.strip().split(" ")
  value = int(value)
  
  if direction == "forward":
    position += value
  elif direction == "up":
    depth -= value
  elif direction == "down":
    depth += value

print (depth*position)
  
# 2
position = 0
depth = 0
aim = 0

for l in lines:
  direction, value = l.strip().split(" ")
  value = int(value)

  if direction == "forward":
    position += value
    depth += aim * value
  elif direction == "up":
    aim -= value
  elif direction == "down":
    aim += value

print (depth*position)