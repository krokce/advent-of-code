with open('day21.txt', 'r') as file:
    monkeys = [l.strip().split(":") for l in file.readlines()]

M = {}
for m in monkeys:
    mt = m[1].split()
    if len(mt) == 1:
        M[m[0]] = [int(mt[0])]
    else:
        M[m[0]] = mt

def solve(m):
    if len(M[m]) == 1:
        return M[m][0]
    elif len(M[m]) == 3:
        if M[m][1] == "+":
            ret = solve(M[m][0]) + solve(M[m][2])
        elif M[m][1] == "-":
            ret = solve(M[m][0]) - solve(M[m][2])
        elif M[m][1] == "*":
            ret = solve(M[m][0]) * solve(M[m][2])
        elif M[m][1] == "/":
            ret = solve(M[m][0]) / solve(M[m][2])
    return int(ret)

print(solve("root"))