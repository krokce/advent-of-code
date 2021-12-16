import math

with open('day16.txt', 'r') as file:
  lines = file.read().strip()

p = bin(int(lines, 16))[2:].zfill(len(lines)*4)

def get_num(p, pointer):
  ret = ""
  while p[pointer] == "1":
    ret += p[pointer+1:pointer+5]
    pointer += 5
  ret += p[pointer+1:pointer+5]
  return pointer+5, int(ret, 2)

def parse_eq(typ, arr):
  if typ == 0: 
    return(sum(arr))
  elif typ == 1: 
    return(math.prod(arr))
  elif typ == 2: 
    return(min(arr))
  elif typ == 3: 
    return(max(arr))
  elif typ == 5:
    return int(arr[0] > arr[1])
  elif typ == 6:
    return int(arr[0] < arr[1])
  elif typ == 7:
    return int(arr[0] == arr[1])

ver_sum = 0

def parse(p, pointer):
  global ver_sum

  ver = int(p[pointer:pointer+3], 2)
  ver_sum += ver
  pointer += 3 

  typ =  int(p[pointer:pointer+3], 2)
  pointer += 3 

  if typ == 4:
    pointer, num = get_num(p, pointer)
    return pointer, num

  elif typ != 4:
    lti = int(p[pointer:pointer+1])
    pointer += 1

    if lti == 0:
      ln = int(p[pointer:pointer+15], 2)
      pointer += 15
      arr = []
      read_ln = pointer + ln
      while True:
        pointer, num = parse(p, pointer)
        if num is not None:
          arr.append(num)
        if pointer == read_ln: 
          break
      return pointer, parse_eq(typ, arr)

    elif lti == 1:
      ln = int(p[pointer:pointer+11], 2)
      pointer += 11
      arr = []
      for _ in range(ln):
        pointer, num = parse(p, pointer)
        if num is not None:
          arr.append(num)
      return pointer, parse_eq(typ, arr)

_, output = parse(p, 0)

# 1
print(ver_sum)

# 2
print(output)