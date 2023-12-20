from itertools import count
import math
from collections import defaultdict

with open("day20.txt", "r") as file:
    lines = [l.strip().split(" -> ") for l in file.readlines()]

MC = {}

for l in lines:
    if l[0][0] == "%":
        MC[l[0][1:]] = {
            "type": "flip_flop",
            "state": False,
            "destinations": l[1].split(", "),
            "sources": [],
        }
    elif l[0][0] == "&":
        MC[l[0][1:]] = {
            "type": "conjunction",
            "state": [],
            "destinations": l[1].split(", "),
            "sources": [],
        }
    else:
        MC[l[0]] = {
            "type": "broadcaster",
            "state": False,
            "destinations": l[1].split(", "),
            "sources": [],
        }

for module_name, module in MC.items():
    for dest in module["destinations"]:
        if dest in MC:
            MC[dest]["sources"].append(module_name)
            if MC[dest]["type"] == "conjunction":
                MC[dest]["state"].append(-1)


def flip_flop(src_module, dst_module, pulse, id):
    ret_pulse = -1
    if pulse == -1:
        MC[dst_module]["state"] = not MC[dst_module]["state"]
        if MC[dst_module]["state"] == False:
            ret_pulse = -1
        else:
            ret_pulse = 1
        for dst in MC[dst_module]["destinations"]:
            queue.append((dst_module, dst, ret_pulse))


def conjunction(src_module, dst_module, pulse, id):
    ret_pulse = 1
    state_index = MC[dst_module]["sources"].index(src_module)
    MC[dst_module]["state"][state_index] = pulse
    if all([state == 1 for state in MC[dst_module]["state"]]):
        ret_pulse = -1
        # 2
        # draw the graph and find the 4 relevant conjunction modules
        # in our case ["lq", "dl", "hf", "hb"]
        # find LCM of conjunction modules cycles
        if dst_module in ["lq", "dl", "hf", "hb"]:
            conjunction_cycles[dst_module] = id - conjunction_cycles[dst_module]
            if len(conjunction_cycles) == 4:
                print(conjunction_cycles)
                print(find_lcm(list(conjunction_cycles.values())))
                exit()
    for dst in MC[dst_module]["destinations"]:
        queue.append((dst_module, dst, ret_pulse))


def consume_queue(src_module, dst_module, pulse, id):
    dst_type = MC[dst_module]["type"]
    if dst_type == "flip_flop":
        flip_flop(src_module, dst_module, pulse, id)
    elif dst_type == "conjunction":
        conjunction(src_module, dst_module, pulse, id)
    else:
        print("error?")


def push_button(id):
    for dst_module in MC["broadcaster"]["destinations"]:
        src_module = "broadcaster"
        queue.append((src_module, dst_module, -1))
    while len(queue):
        src_module, dst_module, pulse = queue.pop(0)
        ret[pulse] += 1
        if dst_module in MC:
            consume_queue(src_module, dst_module, pulse, id)


def find_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


queue = []
ret = {-1: 0, 1: 0}
conjunction_cycles = defaultdict(int)

for i in count():
    push_button(i + 1)
    if i == 999:
        # 1
        print((ret[-1] + 1000) * ret[1])
