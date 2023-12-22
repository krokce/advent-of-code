from collections import defaultdict

with open("day22.txt", "r") as file:
    lines = [
        list(tuple(map(int, k.split(","))) for k in l.strip().split("~"))
        for l in file.readlines()
    ]

B = defaultdict(list)
T = defaultdict(int)

max_block = (0, 0, 0)
for block_id, ((x1, y1, z1), (x2, y2, z2)) in enumerate(lines):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                T[(x, y, z)] = block_id + 1
                B[block_id + 1].append((x, y, z))
                max_block = (
                    max(max_block[0], x),
                    max(max_block[1], y),
                    max(max_block[2], z),
                )


def can_drop(block_id):
    for bx, by, bz in B[block_id]:
        if (bx, by, bz - 1) in T and T[(bx, by, bz - 1)] != block_id:
            return False
        if bz == 1:
            return False
    return True


def drop(block_id):
    new_block = []
    for bx, by, bz in B[block_id]:
        del T[(bx, by, bz)]
        T[(bx, by, bz - 1)] = block_id
        new_block.append((bx, by, bz - 1))
    B[block_id] = new_block


# sort by z-axis lowest blocks first
def sorted_blocks():
    ret = []
    for block_id, blocks in B.items():
        ret.append((block_id, min([z for x, y, z in blocks])))
    return [b[0] for b in sorted(ret, key=lambda e: e[1])]


def bricks_above(block_id):
    ret = set()
    for bx, by, bz in B[block_id]:
        if (bx, by, bz + 1) in T and T[(bx, by, bz + 1)] != block_id:
            ret.add(T[(bx, by, bz + 1)])
    return ret


def bricks_below(block_id):
    ret = set()
    for bx, by, bz in B[block_id]:
        if (bx, by, bz - 1) in T and T[(bx, by, bz - 1)] != block_id:
            ret.add(T[(bx, by, bz - 1)])
    return ret


def can_disintegrate(block_id):
    for above in bricks_above(block_id):
        if len(bricks_below(above) - {block_id}) == 0:
            return False
    return True


def do_desintegrate(block_id):
    for bx, by, bz in B[block_id]:
        del T[(bx, by, bz)]
    del B[block_id]


# settle down the tower
for b in sorted_blocks():
    while can_drop(b):
        drop(b)

# 1
ret = 0
for b in sorted_blocks():
    if can_disintegrate(b):
        ret += 1
print(ret)

# 2
ret = 0
tower = T
blocks = B
for block in B.keys():
    T = tower.copy()
    B = blocks.copy()
    do_desintegrate(block)
    for b in sorted_blocks():
        if can_drop(b):
            do_desintegrate(b)
            ret += 1

print(ret)
