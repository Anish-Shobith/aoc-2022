dic = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

def load():
    return open('input.txt').read().split('\n')
        
def part1(data = load()):
        score = 0
        for i in data:
            opp, me = [dic[j] for j in i.split(" ")]
            if ((me - opp) % 3) == 1:
                score += 6
            elif me == opp:
                score += 3
            score += [1, 2, 3][me]
        return score

def part2(data = load()):
    score = 0
    dic.update({"X": -1, "Y": 0, "Z": 1})
    for i in data:
        opp, me = [dic[j] for j in i.split(" ")]
        score += (me + 1) * 3
        score += [1, 2, 3][(opp + me) % 3]
    return score


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')