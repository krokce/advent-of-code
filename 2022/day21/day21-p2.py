with open('day21.txt', 'r') as file:
    monkeys = [l.strip().split(":") for l in file.readlines()]

M = {}
for m in monkeys:
    mt = m[1].split()
    if len(mt) == 1:
        M[m[0]] = [int(mt[0])]
    else:
        M[m[0]] = mt

def solve(m, h):
    if m == "humn":
        if h is None:
            return m[0]
        else:
            return h
    if len(M[m]) == 1:
        return M[m][0]
    elif len(M[m]) == 3:
        if M[m][1] == "+":
            ret = solve(M[m][0], h) + solve(M[m][2], h)
        elif M[m][1] == "-":
            ret = solve(M[m][0], h) - solve(M[m][2], h)
        elif M[m][1] == "*":
            ret = solve(M[m][0], h) * solve(M[m][2], h)
        elif M[m][1] == "/":
            ret = solve(M[m][0], h) / solve(M[m][2], h)
    return int(ret)

target = solve(M["root"][2], None)
attempt = 1
prev_delta = target
while True:
    sign = 1
    delta = solve(M["root"][0], attempt) - target
    # print(int(attempt), delta)
    if delta == 0:
        print(int(attempt))
        break
    else:
        if abs(delta) >= abs(prev_delta):
            sign *= -1
            delta = delta / 2
        attempt = attempt - sign * abs(delta) * 0.01
    prev_delta = delta