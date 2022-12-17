import re

with open('day16.txt', 'r') as file:
    input = [l.strip() for l in file.readlines()]

V = {}
C = {}

def distance(a,b):
    return abs(a[0]-b[0]) +  abs(a[1]-b[1])

for scan_line in input:
    parsed_line = [i for i in re.findall(r"[\d]+|[A-Z]{2}", scan_line)]
    valve = parsed_line.pop(0)
    flow_rate = int(parsed_line.pop(0))
    tunnels = parsed_line
    V[valve] = flow_rate
    C[valve] = tunnels

D = {}

max_solution = 0

def solve(valve, my_time, preasure_released, preasure_per_minute, closed_valves):
    global max_solution

    if my_time == 30:
        if preasure_released > max_solution:
            max_solution = preasure_released
    else:
        for t in range(my_time, 30):
            D[valve, t, tuple(closed_valves)]  = 1

        if valve in closed_valves:
            next_closed_valves = closed_valves.copy()
            next_closed_valves.remove(valve)
            if (valve, my_time, tuple(next_closed_valves)) not in D:
                solve(valve, my_time+1, preasure_released + preasure_per_minute, preasure_per_minute+V[valve], next_closed_valves)

        for next_valve in C[valve]:
            if (next_valve, my_time, tuple(closed_valves)) not in D:
                solve(next_valve, my_time+1, preasure_released + preasure_per_minute, preasure_per_minute, closed_valves)

        solve(valve, my_time+1, preasure_released + preasure_per_minute, preasure_per_minute, closed_valves)

solve("AA", 0, 0, 0, sorted([v for v,k in V.items() if k>0]))
print(max_solution)
