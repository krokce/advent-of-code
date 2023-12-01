from collections import Counter
input = "254032-789860"

start, end = [int(i) for i in input.split("-")]

def is_valid1(i):

  stri = str(i)
  fl = stri[0]
  repeats = {}

  for j in range(1, len(stri)):
    if int(stri[j]) < int(fl):
      return False

    if stri[j] == fl:
      if stri[j] in repeats:
        repeats[stri[j]] += 1
      else:
        repeats[stri[j]] = 1

    fl = stri[j]

  if len(repeats) == 0:
    return False

  return True

def is_valid2(i):

  stri = str(i)
  fl = stri[0]
  repeats = {}

  for j in range(1, len(stri)):
    if int(stri[j]) < int(fl):
      return False

    if stri[j] == fl:
      if stri[j] in repeats:
        repeats[stri[j]] += 1
      else:
        repeats[stri[j]] = 1

    fl = stri[j]

  if len(repeats) == 0 or len([i for i in repeats.values() if i==1]) == 0:
    return False

  return True

ret1 = 0
ret2 = 0
for i in range(start, end):
  if is_valid1(i):
    ret1 += 1
  if is_valid2(i):
    ret2 += 1
    
print(ret1)
print(ret2)