from collections import deque

with open('day20.txt', 'r') as file:
    numbers = [int(l.strip())*811589153 for l in file.readlines()]

L = deque(enumerate(numbers))

for j in range(10):
    for i in range(len(L)):
        while L[0][0] != i:
            L.append(L.popleft())

        if L[0][1] != 0:

            v = L.popleft()
            offset = v[1]
            
            # move left
            if offset < 0:
                for i in range(abs(offset)%len(L)):
                    L.appendleft(L.pop())
                L.append(v)

            # move right
            if offset > 0:
                for i in range(abs(offset)%len(L)):
                    L.append(L.popleft())
                L.appendleft(v)

while L[0][1] != 0:
    L.append(L.popleft())

print(L[1000%len(L)][1] + L[2000%len(L)][1] + L[3000%len(L)][1])