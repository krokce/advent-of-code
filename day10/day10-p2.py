with open('day10.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

err = {")":1, "]":2, "}":3, ">":4}
pair = {"(":")", "[":"]", "{":"}", "<":">"}
ret = []

for l in input:
  expect = []
  for c in l:
    if c in pair:
      expect.append(pair[c])
    else:
      b = expect.pop()
      if b != c:
        expect = []
        break
  if len(expect) > 0:
    tmp = 0
    while len(expect) > 0:
      b = expect.pop()
      tmp = tmp * 5 + err[b]
    ret.append(tmp)

print(sorted(ret)[len(ret)//2])