import re

def load():
    return [x.strip().split('\n') for x in open('input.txt').read().split('\n\n')]

def ints(string):
    return list(map(int, re.findall(r"-?[0-9]+", string)))

def part1():
    m, cmds = load()
    N = ints(m[-1])[-1]
    stacks = [[] for _ in range(N)]
    for line in list(reversed(m))[1:]:
        for i in range(N):
            j = 1+i*4
            if line[j:j+1] not in (" ", ""):
                stacks[i].append(line[j])

    for cmd in cmds:
        cnt, from_, to = ints(cmd)
        for _ in range(cnt):
            c = stacks[from_-1].pop()
            stacks[to-1].append(c)

    return "".join([s[-1] for s in stacks])

def part2():
    m, cmds = load()
    N = ints(m[-1])[-1]
    stacks = [[] for _ in range(N)]
    for line in list(reversed(m))[1:]:
        for i in range(N):
            j = 1+i*4
            if line[j:j+1] not in (" ", ""):
                stacks[i].append(line[j])

    for cmd in cmds:
        cnt, from_, to = ints(cmd)
        moved = stacks[from_-1][-cnt:]
        del stacks[from_-1][-cnt:]
        stacks[to-1].extend(moved)

    return "".join([s[-1] for s in stacks])

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')