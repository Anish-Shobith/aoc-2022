def split(data):
    return sum([int(x) for x in data.split('\n')])

def load():
    return list(map(split, open('input.txt').read().split('\n\n')))

def part1(elves = load()):
    return max(elves)

def part2(elves = load()):
    return sum(list(reversed(sorted(elves)))[:3])

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')