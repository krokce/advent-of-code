import re
import numpy as np
import itertools
from copy import deepcopy as dc

with open('day24.txt', 'r') as file:
  instructions = [k.strip().split(" ") for k in file.readlines()]

for n in range(len(instructions)):
  try:
    instructions[n][2] = int(instructions[n][2])
  except:
    pass
  try:
    instructions[n][1] = int(instructions[n][1])
  except:
    pass

x,y,z = 0,0,0

def run(input):
  global x
  global y
  global z
  x,y,z = 0,0,0

  input_cnt = 0
  for i in instructions:
    if i[0] == "inp":
      exec("global x; global y; global z;"+i[1]+"="+input[input_cnt])
      input_cnt += 1
      continue
    if i[0] == "add":
      exec("global x; global y; global z;"+i[1]+"="+str(i[1])+"+"+str(i[2]))
      continue
    if i[0] == "mul":
      exec("global x; global y; global z;"+i[1]+"="+str(i[1])+"*"+str(i[2]))
      continue
    if i[0] == "div":
      if i[2] == 0:
        continue
      exec("global x; global y; global z;"+i[1]+"="+str(i[1])+"//"+str(i[2]))
      continue
    if i[0] == "mod":
      if i[2] < 0:
        continue
      exec("global x; global y; global z;"+i[1]+"="+str(i[1])+"%"+str(i[2]))
      continue
    if i[0] == "eql":
      exec("global x; global y; global z;"+i[1]+"=int("+str(i[1])+"=="+str(i[2])+")")
      continue
  return x,y,z

# Manual de-compile
print(run("93959993429899"))
print(run("11815671117121"))
