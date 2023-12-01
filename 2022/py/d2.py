
score = 0

def get_score(move):
    return {
        'X': 1,
        'Y': 2,
        'Z': 3
    }[move]

def map_other(move):
    return {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }[move]

def win_score(other, me):
    if get_score(other) == get_score(me):
        return 3
    # rock, paper
    if other == 'X' and me == 'Y':
        return 6
    # paper, scissor
    if other == 'Y' and me == 'Z':
        return 6
    # scissor, rock
    if other == 'Z' and me == 'X':
        return 6
    return 0
    
while True:
    try:
        line = input()
    except EOFError:
        break
    print(line, len(line), line.split())
    if len(line.split()) == 2:
        other, me = line.split()
        other = map_other(other)
        score += get_score(me)
        score += win_score(other, me)
    else:
        break

print(score)
