import re
import math

with open('day06.txt', 'r') as file:
	lines = [l.strip().split(':') for l in file.readlines()]

times = list(map(int, re.findall(r'\d+', lines[0][1])))
distances = list(map(int, re.findall(r'\d+', lines[1][1])))

ret = []
for race_id, time in enumerate(times):
	wins = 0
	for t in range(time+1):
		if t * (time-t) > distances[race_id]:
			wins += 1
	ret.append(wins)

#1
print(math.prod(ret))

#2
time = int (''.join(map(str, times)))
distance = int (''.join(map(str, distances)))

# solutions of the quadratic equation [-x^2+time*x-distance = 0]
s1 = (-1*time + math.sqrt(math.pow(time, 2) - 4*distance))/(-2)
s2 = (-1*time - math.sqrt(math.pow(time, 2) - 4*distance))/(-2)

print(math.ceil(s2 - s1))