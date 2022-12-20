import re
import math
from collections import defaultdict

with open('day19.txt', 'r') as file:
    input = [l.strip().split(":") for l in [l for l in file.readlines()] if l.strip()]

material_id = ["ore", "clay", "obsidian", "geode"]

blueprint = {}
for l in input:
    blueprint_id = int(l[0].split()[1])
    blueprint[blueprint_id] = list()
    for r in l[1].split("."):
        if r == "":
            continue
        
        robot_type = re.findall(r"([\w]+) robot", r)[0]
        robot_cost = re.findall(r"([\d]+ [(ore)|(clay)|(obsidian)]+)", r)
        rc = [0] * 4
        for cost, resource in [c.split() for c in robot_cost]:
            rc[material_id.index(resource)] = int(cost)
        
        blueprint[blueprint_id].append({
            "robot_type": robot_type,
            "robot_type_id": material_id.index(robot_type),
            "cost": rc,
            "cost_txt": robot_cost
        })

def collect_resources(resources, robots):
    for i in range(len(resources)):
        resources[i] += robots[i]

def order_robot(blueprint_id, robot_id, resources, production):
    cost = blueprint[blueprint_id][robot_id]["cost"]
    for i in range(len(cost)):
        resources[i] -= cost[i]
    production.append(robot_id)

def can_order_robot(blueprint_id, robot_id, resources):
    cost = blueprint[blueprint_id][robot_id]["cost"]
    for i in range(len(cost)):
        if resources[i] - cost[i] < 0:
            return False
    return True

def pick_up_robot(production, robots):
    if len(production) > 0:
        robot_id = production.pop()
        robots[robot_id] += 1

def possible_orders(blueprint_id, resources):
    ret = []
    for robot_id in range(len(resources)):
        if can_order_robot(blueprint_id, robot_id, resources):
            ret.append(robot_id)
    return(ret)

D = {}
MAX = defaultdict(int)

def solve(resources, robots, blueprint_id, my_time):
    if my_time == 32:
        if resources[3] > MAX[blueprint_id]:
            MAX[blueprint_id] = resources[3]
    else:
        key = (tuple(resources[0:3]), tuple(robots[0:3]))
        if key in D and D[key] <= my_time:
            return
        
        D[key] = my_time

        next_orders = possible_orders(blueprint_id, resources)
        
        if 3 in next_orders:
            next_orders = [3]
        else:
            next_orders.append(-1)

        for robot_id in next_orders:
            if 0 <= robot_id < 3 and robots[robot_id] >= max([r["cost"][robot_id] for r in blueprint[blueprint_id]]):
                continue

            if 0 <= robot_id < 3 and resources[robot_id] >= max([r["cost"][robot_id] for r in blueprint[blueprint_id]]) * (32-my_time):
                continue
                        
            tmp_resources = resources.copy()
            tmp_robots = robots.copy()
            tmp_production = []
            if robot_id >= 0:
                order_robot(blueprint_id, robot_id, tmp_resources, tmp_production)
            collect_resources(tmp_resources, tmp_robots)
            pick_up_robot(tmp_production, tmp_robots)
            solve(tmp_resources, tmp_robots, blueprint_id, my_time+1)

for bid, b in blueprint.items():
    if bid < 4:
        robots = [1, 0, 0, 0]
        resources = [0, 0, 0, 0]
        D = {}
        solve(resources=[0, 0, 0, 0], robots=[1, 0, 0, 0], blueprint_id=bid, my_time=0)
        print(bid, MAX[bid])

#2
print(math.prod([geodes for bid, geodes in MAX.items()]))