input = open(0).read();

input = [list(map(int, line.split(" "))) for line in input.splitlines()]

def is_safe(line: list[int]) -> bool:
    increasing = line[1] > line[0]
    prev = line[0]
    for next in line[1:]:
        change = abs(next - prev)
        if change > 3 or change < 1:
            return False
        if next > prev and increasing:
            prev = next
        elif next < prev and not increasing:
            prev = next
        else:
            return False
    return True

def is_safe_dampened(line: list[int]) -> bool:
    for x in range(len(line)):
        line_copy = line.copy()
        del line_copy[x]
        if is_safe(line_copy):
            return True
    return False

safe = 0
safe_with_dampener = 0
for line in input:
    if is_safe(line):
        safe += 1
        safe_with_dampener += 1
    elif is_safe_dampened(line):
        safe_with_dampener += 1
print(safe, safe_with_dampener)