import math

with open('day18.txt', 'r') as file:
  lines = [i.strip() for i in file.readlines()]

T = {}

def snail_tree(T, arr, level, parent):
  element_id = len(T)
  T[element_id] = {
      "level": level, 
      "parent": parent,
      "left": None,
      "right": None,
      "value": arr
    }
  if isinstance(arr, list):
    T[element_id]["value"] = None
    T[element_id]["left"] = snail_tree(T, arr[0], level+1, element_id)
    T[element_id]["right"] = snail_tree(T, arr[1], level+1, element_id)
  return element_id

def find_update_parent(T, element_id):
  
  parent = T[element_id]["parent"]
  arr = snail_parse_order(T, 0, [])
  element_id_idx = arr.index(element_id)

  if T[parent]["left"] == element_id:
    arr = reversed(arr[:element_id_idx])
  else:
    arr = arr[element_id:]

  for k in arr:
    if T[k]["value"] is not None:
      return k
  return None


def snail_parse_order(T, id, ret):

  if T[id]["left"] is None and T[id]["right"] is None:
    if id not in ret:
      ret.append(T[id]["right"])

  if T[id]["left"] is not None:
    if T[id]["left"] not in ret:
      ret.append(T[id]["left"])
    snail_parse_order(T, T[id]["left"], ret) 

  if T[id]["right"] is not None:
    if T[id]["right"] not in ret:
      ret.append(T[id]["right"])
    snail_parse_order(T, T[id]["right"], ret) 

  return ret

def explode_snail(T):
  for k in snail_parse_order(T, 0,[]):
    v = T[k]
    if v["level"] == 4 and v["left"] is not None and v["right"] is not None:

      # get values 
      l_id = v["left"]
      r_id = v["right"]

      l_val = T[l_id]["value"]
      r_val = T[r_id]["value"]

      l_upd_id = find_update_parent(T, l_id)
      r_upd_id = find_update_parent(T, r_id)
      
      # update left    
      if l_upd_id is not None:
        T[l_upd_id]["value"] += l_val
      else:
        T[k]["left"] = None
        T[k]["right"] = None
        T[k]["value"] = 0

      # update right
      if r_upd_id is not None:
        T[r_upd_id]["value"] += r_val
      else:
        T[k]["left"] = None
        T[k]["right"] = None
        T[k]["value"] = 0

      # delete node
      del T[l_id]
      del T[r_id]
      if l_upd_id is not None and r_upd_id is not None:
        T[k]["left"] = None
        T[k]["right"] = None
        T[k]["value"] = 0        
      return True
  return False

def split_snail(T):
  elements = snail_parse_order(T, 0,[])
  max_id = max(elements)
  for k in elements:
    v = T[k]
    if v["left"] is None and v["right"] is None and v["value"] > 9:
      l_val = math.floor(v["value"]/2)
      r_val = math.ceil(v["value"]/2)

      T[k]["left"] = max_id + 1
      T[k]["right"] = max_id + 2
      T[k]["value"] = None

      T[max_id + 1] = {
        "level": v["level"]+1, 
        "parent": k,
        "left": None,
        "right": None,
        "value": l_val
      }

      T[max_id + 2] = {
        "level": v["level"]+1, 
        "parent": k,
        "left": None,
        "right": None,
        "value": r_val
      }

      return True
  return False

def snail_to_string(T):
  s = ""
  level = 0
  for k in snail_parse_order(T, 0, []):
    if T[k]["level"] > level:
      s += "[" * (T[k]["level"] - level)
    elif T[k]["level"] < level:
      s += "]" * (level - T[k]["level"]) + ","
    else:
      s += ","
    if T[k]["value"] is not None:
      s += str(T[k]["value"])
    level = T[k]["level"]
  s += "]" * level
  return s

def magnitude(T, id, s):
  if T[id]["value"] is None:
    return s + 3 * magnitude(T, T[id]["left"], s) + 2 * magnitude(T, T[id]["right"], s)
  else:
    return s + T[id]["value"]

snail = []
T = {}

for s in lines:
  if len(snail) == 0:
    snail = eval(s)
  else: 
    snail = [snail, eval(s)]
  T = {}
  snail_tree(T, snail, 0, None)

  exploded = True
  splitted = False

  while exploded or splitted:
    T = {}
    snail_tree(T, snail, 0, None)
    exploded = explode_snail(T)
    snail = eval(snail_to_string(T))
    if not exploded:
      splitted = split_snail(T)
      snail = eval(snail_to_string(T))

# 1
print(magnitude(T, 0, 0))

# 2
max_magnitude = 0
for s1 in lines:
  for s2 in lines:
    if s1 != s2:
      snail = eval("[" + s1 + "," + s2 + "]")
      T = {}
      snail_tree(T, snail, 0, None)
      exploded = True
      splitted = False
      while exploded or splitted:
        T = {}
        snail_tree(T, snail, 0, None)
        exploded = explode_snail(T)
        snail = eval(snail_to_string(T))
        if not exploded:
          splitted = split_snail(T)
          snail = eval(snail_to_string(T))
      max_magnitude = max(max_magnitude, magnitude(T, 0, 0))    
print(max_magnitude)