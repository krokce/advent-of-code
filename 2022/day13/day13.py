from functools import cmp_to_key

with open('day13.txt', 'r') as file:
    input = [eval(l) for l in [lines.strip() for lines in file.readlines()] if l != ""]

def normalize_types(left, right):
    if type(left) is int:
        left = [left]
    if type(right) is int:
        right = [right]
    return left, right

def comp(left, right):
    if type(left) != type(right):
        l, r = normalize_types(left, right)
        return comp(l, r)
 
    if type(left) is int and type(right) is int: 
        if left < right:
            return -1 
        else:
            return 1

    if len(right) == 0 and len(left) > 0:
        return 1
        
    for i in range(len(right)):
        if i == len(left):
            return -1
        if left[i] != right[i]:
            return comp(left[i], right[i])
    return 1

right_order = []
idx = 0

for i in range(1, len(input), 2):
    idx += 1
    left = input[i-1]
    right = input[i]
    
    if comp(left, right) < 0:
        right_order.append(idx)

#1
print(sum(right_order))

#2
input.append([[2]])
input.append([[6]])
input.sort(key=cmp_to_key(comp))
print((input.index([[2]])+1) * (input.index([[6]])+1))