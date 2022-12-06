def load():
    return open('input.txt').read().strip()

def part1(data = load()):
    for _ in range(2):
        for i in range(len(data) - 4):
            if len(set(data[i:i+4])) == 4:
                return i + 4

def part2(data = load()):
    for _ in range(2):
        for i in range(len(data) - 14):
            if len(set(data[i:i+14])) == 14:
                return i + 14

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')