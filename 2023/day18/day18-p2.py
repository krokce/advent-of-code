with open("day18.txt", "r") as file:
    lines = [l.strip().split(" ") for l in file.readlines()]

# The Shoelace Algorithm
# https://www.101computing.net/the-shoelace-algorithm/
    
def shoelace_algorithm(vertices):
  #A function to apply the Shoelace algorithm
  numberOfVertices = len(vertices)
  sum1 = 0
  sum2 = 0
  
  for i in range(0,numberOfVertices-1):
    sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
    sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  
  #Add xn.y1
  sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
  #Add x1.yn
  sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
  
  area = abs(sum1 - sum2) / 2
  return area

# R, D, L, U
directions = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
position = (0, 0)

T1 = [(0,0)]
T2 = [(0,0)]
l1 = 0
l2 = 0
for direction, steps, color in lines:
    steps = int(steps)
    val = color.replace("(#", "").replace(")", "")
    s = int(val[0:-1], 16)
    d = int(val[-1:], 16)
    
    p1 = (T1[-1][0] + steps*directions[direction][0], T1[-1][1] + steps*directions[direction][1])
    T1.append(p1)
    l1 += int(steps)

    p2 = (T2[-1][0] + s*D[d][0], T2[-1][1] + s*D[d][1])
    T2.append(p2)
    l2 += int(s)

#1
print(int(shoelace_algorithm(T1) + l1/2 + 1))

#2
print(int(shoelace_algorithm(T2) + l2/2 + 1))