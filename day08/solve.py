input = open(0).read().split();

antinodes = set()
inline_antinodes = set()

def is_in_map(x, y):
    return y  < len(input) and x < len(input[y]) and x >= 0 and y >= 0
        

def add_antinode(x1, y1, x2, y2):
    global antinodes
    base_x_offset = x2 - x1
    base_y_offset = y2 - y1
    if is_in_map(x2 + base_x_offset, y2 + base_y_offset):
        antinodes.add((x2 + base_x_offset, y2 + base_y_offset))
    if is_in_map(x1 - base_x_offset, y1 - base_y_offset):
        antinodes.add((x1 - base_x_offset, y1 - base_y_offset))
    
    x_offset = 0
    y_offset = 0
    while is_in_map(x2 + x_offset, y2 + y_offset) or is_in_map(x1 - x_offset, y1 - y_offset):
        if is_in_map(x2 + x_offset, y2 + y_offset):
            inline_antinodes.add((x2 + x_offset, y2 + y_offset))
        if is_in_map(x1 - x_offset, y1 - y_offset):
            inline_antinodes.add((x1 - x_offset, y1 - y_offset))
        x_offset += base_x_offset
        y_offset += base_y_offset


def check(x: int, y: int):
    global input
    antinode_type = input[y][x]
    for other_y,l in enumerate(input):
        for other_x,c in enumerate(l):
            if other_x == x and other_y == y:
                continue

            if c == antinode_type:
                add_antinode(x, y, other_x, other_y)

for y,l in enumerate(input):
    for x,c in enumerate(l):
        if c == ".":
            continue
        check(x, y)

a = len(antinodes)
b = len(inline_antinodes)

print(a, b)

