score = 0

def act(move):
    return {
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
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
    

def get_move_to_play(other, action):
    if action == 'draw':
        return other
    winning = {
        'X': 'Y',
        'Y': 'Z',
        'Z': 'X',
    }
    if action == 'lose':
        for i in winning:
            if i != winning[other] and i != other:
                return i
    return winning[other]

def get_score(move):
    return {
        'X': 1,
        'Y': 2,
        'Z': 3
    }[move]

while True:
    try:
        line = input()
    except EOFError:
        break
    print(line, len(line), line.split())
    if len(line.split()) == 2:
        other, me = line.split()
        other = map_other(other)
        my_move = get_move_to_play(other, act(me))
        score += get_score(my_move)
        score += win_score(other, my_move)
    else:
        break

print(score)
