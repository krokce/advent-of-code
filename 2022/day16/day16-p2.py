import re
import heapq
from itertools import product

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
heapq.heappush(Q, (0, ["AA", "AA"], 0, set()))
visited = set()

total_time = 26
penalty = 111
last_time = 0
while True:
    score, current_valves, my_time, open_valves = heapq.heappop(Q)
    
    if my_time == total_time:
        print(total_time*penalty-score)
        break
        
    actions = []
    
    for player_id, current_valve in enumerate(current_valves):

        # open current valve
        if current_valve not in open_valves and V[current_valve] > 0:
            actions.append((player_id, "open", current_valve))
        
        # visit connected valves
        for next_valve in C[current_valve]:
            actions.append((player_id, "visit", next_valve))

    for (player_id_a, action_a, valve_a), (player_id_b, action_b, valve_b) in list(product([action for action in actions if action[0] == 0], [action for action in actions if action[0] == 1])):

        if player_id_a == player_id_b:
            continue

        if valve_a == valve_b:
            continue

        add_score = penalty
        key = frozenset({valve_a, valve_b})
        next_open = open_valves.copy()

        if action_a == "open":
            next_open.add(valve_a)
            add_score += -V[valve_a] * (total_time - my_time - 1)

        if action_b == "open":
            next_open.add(valve_b)
            add_score += -V[valve_b] * (total_time - my_time - 1)

        if (key, my_time, score) in visited:
            continue

        visited.add((key, my_time, score))
        heapq.heappush(Q, (score+add_score, [valve_a, valve_b], my_time+1, next_open))

        if my_time > last_time:
            print(my_time*penalty-score-add_score, my_time, open_valves)
            last_time = my_time