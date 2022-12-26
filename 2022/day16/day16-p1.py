import re
import heapq

with open('day16.txt', 'r') as file:
    input = [l.strip() for l in file.readlines()]

V = {}
C = {}

for scan_line in input:
    parsed_line = [i for i in re.findall(r"[\d]+|[A-Z]{2}", scan_line)]
    valve = parsed_line.pop(0)
    flow_rate = int(parsed_line.pop(0))
    tunnels = parsed_line
    V[valve] = flow_rate
    C[valve] = tunnels


Q = []
heapq.heappush(Q, (0, "AA", 0, set()))
visited = set()

total_time = 30
penalty = 111
while True:
    score, current_valve, my_time, open_valves = heapq.heappop(Q)
    
    if my_time == total_time:
        print(total_time*penalty-score)
        break

    actions = []

    # open current valve
    if current_valve not in open_valves and V[current_valve] > 0:
        actions.append(("open", current_valve))
    
    # visit connected valves
    for next_valve in C[current_valve]:
        actions.append(("visit", next_valve))

    for action, valve in actions:
        add_score = penalty

        next_open = open_valves.copy()

        if action == "open":
            next_open.add(valve)
            add_score += -V[valve] * (total_time - my_time - 1)
        
        if (valve, my_time, score) in visited:
            continue

        visited.add((valve, my_time, score))
        heapq.heappush(Q, (score+add_score, valve, my_time+1, next_open))