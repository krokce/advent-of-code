with open('day10.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

err = {")":3, "]":57, "}":1197, ">":25137}
pair = {"(":")", "[":"]", "{":"}", "<":">"}
ret = 0

for l in input:
  expect = []
  for c in l:
    if c in pair:
      expect.append(pair[c])
    else:
      b = expect.pop()
      if b != c:
        ret += err[c]
        break
print(ret)