def load():
    return open('input.txt').read().split('\n')

def part1(lines = load()):
    count = 0
    for line in lines:
        first, second = line.split(",")
        fs, fl = first.split("-")
        ss, sl = second.split("-")

        fs, fl, ss, sl = int(fs), int(fl), int(ss), int(sl)

        if (fs <= ss and fl >= sl) or (ss <= fs and sl >= fl):
            count += 1
    return count

def part2(lines = load()):
    count = 0
    for line in lines:
        first, second = line.split(",")
        fs, fl = first.split("-")
        ss, sl = second.split("-")

        fs, fl, ss, sl = int(fs), int(fl), int(ss), int(sl)

        if not ((fl < ss) or (sl < fs)):
            count += 1
    return count

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')