def load():
    return open('input.txt').read().split('\n')

def priortiy(c):
    e = ord(c)
    return e - 96 if e > 96 else e - 38


def part1(data = load()):
    s = 0
    for line in data:
        mid = len(line) // 2
        e, = set(line[0:mid]) & set(line[mid:])
        s += priortiy(e)
    return s

def part2(data = load()):
    s = 0
    p = pp = None
    for line in data:
        if p and pp:
            c, = p & pp & set(line)
            s += priortiy(c)
            p = pp = None
        else:
            pp = p
            p = set(line)
    return s

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')