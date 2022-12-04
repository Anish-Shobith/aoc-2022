def load():
    return open('input.txt').read().split('\n')

def part1(lines = load()):
    count = 0
    for line in lines:
        first, second = line.split(",")
        fs, fl = list(map(int, first.split("-")))
        ss, sl = list(map(int, second.split("-")))

        if (fs <= ss and fl >= sl) or (ss <= fs and sl >= fl):
            count += 1
    return count

def part2(lines = load()):
    count = 0
    for line in lines:
        first, second = line.split(",")
        fs, fl = list(map(int, first.split("-")))
        ss, sl = list(map(int, second.split("-")))

        if not ((fl < ss) or (sl < fs)):
            count += 1
    return count

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')