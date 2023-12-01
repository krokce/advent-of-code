with open('day01.txt', 'r') as file:
  input = file.readlines()

ret = 0
for l in input:
  ret += int(int(l.strip()) / 3) - 2
print(ret)

def get_fuel(mass):
  return int(mass / 3) - 2

ret = 0
for l in input:
  mass = int(l.strip())
  k = get_fuel(mass)
  total_fuel = k
  while k > 0:
    k = get_fuel(k)
    if k > 0:
      total_fuel += k
  ret += total_fuel

print(ret)
