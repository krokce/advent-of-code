with open('day02.txt', 'r') as file:
  input = [l.strip() for l in file.readlines()]

# game score + hand score
S1 = {
  'A X': 3 + 1, 
  'B X': 0 + 1,
  'C X': 6 + 1,
  'A Y': 6 + 2,
  'B Y': 3 + 2,
  'C Y': 0 + 2,
  'A Z': 0 + 3,
  'B Z': 6 + 3,
  'C Z': 3 + 3,
}

S2 = {
  'A X': 0 + 3,
  'B X': 0 + 1,
  'C X': 0 + 2,
  'A Y': 3 + 1,
  'B Y': 3 + 2,
  'C Y': 3 + 3,
  'A Z': 6 + 2,
  'B Z': 6 + 3,
  'C Z': 6 + 1,
}

#1
print(sum([S1[i] for i in input]))

#2
print(sum([S2[i] for i in input]))