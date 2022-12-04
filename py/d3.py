total = 0
def get_score(char: str) -> int:
    if char.lower() == char:
        return ord(char) - ord('a') + 1
    else:
        return ord(char) - ord('A') + 27

for j in range(100):
    # try:
    badges = set(input().strip())
    # except EOFError:
    #     print(j)
    #     break
    badges.intersection_update(set(input().strip()))
    badges.intersection_update(set(input().strip()))
 
    common = next(iter(badges))
    total += get_score(common)
print(total)
