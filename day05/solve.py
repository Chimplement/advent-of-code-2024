from functools import cmp_to_key

input = open(0).read();

input = input.split("\n\n")
rules = [tuple(map(int, line.split("|")))for line in input[0].splitlines()]
updates = [list(map(int, line.split(",")))for line in input[1].splitlines()]

def check(l: list[int], r: list[tuple[int]]) -> bool:
    for i, n in enumerate(l):
        number_before = set([rule[0] for rule in r if rule[1] == n])
        for n2 in l[i:]:
            if n2 in number_before:
                return False
    return True

def fix(l: list[int], r: list[tuple[int]]):
    return sorted(
        l,
        key = cmp_to_key(lambda a, b: a in set([rule[0] for rule in r if rule[1] == b]) and 1 or -1),
    )

a = 0
b = 0

for update in updates:
    if check(update, rules):
        a += update[int(len(update) / 2)]
    else:
        fixed_update = fix(update, rules)
        b += fixed_update[int(len(fixed_update) / 2)]

print(a, b)

