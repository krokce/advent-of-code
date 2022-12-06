with open('day06.txt', 'r') as file:
  input = file.readline()

def get_marker(n):
  for i in range(n, len(input)):
    if len(set(input[i-n: i])) == n:
      return i

#1
print(get_marker(4))

#2
print(get_marker(14))