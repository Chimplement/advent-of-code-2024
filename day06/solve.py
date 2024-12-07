input = list(map(list, open(0).read().splitlines()));

guard_x = 0
guard_y = 0
guard_dir = 0
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for y,l in enumerate(input):
    for x,c in enumerate(l):
        if c == "^":
            guard_x = x
            guard_y = y
            break

visited_cells = set()
visited_cells.add((guard_x, guard_y))
visited_cells_by_direction = [set(), set(), set(), set()]
visited_cells_by_direction[0].add((guard_x, guard_y))
possible_blocks = set()
bounced = 4

def guard_move() -> bool:
    global guard_y, guard_dir, guard_x, dirs, bounced
    if not 0 <= dirs[guard_dir][1] + guard_y < len(input):
        return False
    if not 0 <= dirs[guard_dir][0] + guard_x < len(input[guard_y]):
        return False
    if input[guard_y + dirs[guard_dir][1]][dirs[guard_dir][0] + guard_x] == '#':
        guard_dir += 1
        guard_dir %= len(dirs)
        bounced += 1
    else:
        guard_x += dirs[guard_dir][0]
        guard_y += dirs[guard_dir][1]
    return True

def crossed_path() -> bool:
    global guard_y, guard_dir, guard_x, dirs
    if (guard_x, guard_y) in visited_cells_by_direction[(guard_dir + 1) % len(dirs)]:
        if not (guard_x + dirs[guard_dir][0], guard_y + dirs[guard_dir][1]) in visited_cells:
            return True
    return False

def rotate_would_meet_path() -> bool:
    global guard_y, guard_dir, guard_x, dirs
    block_y = dirs[guard_dir][1] + guard_y 
    block_x = dirs[guard_dir][0] + guard_x
    new_dir = (guard_dir + 1) % len(dirs)
    new_guard_x = guard_x
    new_guard_y = guard_y
    bounce_limit = 10000
    visited_cells_by_direction_during_test = [set(), set(), set(), set()]
    visited_cells_by_direction_during_test[new_dir].add((new_guard_x, new_guard_y))
    while bounce_limit > 0:
        if not 0 <= dirs[new_dir][1] + new_guard_y < len(input):
            return False
        if not 0 <= dirs[new_dir][0] + new_guard_x < len(input[new_guard_y]):
            return False
        if input[new_guard_y + dirs[new_dir][1]][dirs[new_dir][0] + new_guard_x] == '#' or (dirs[new_dir][0] + new_guard_x == block_x and dirs[new_dir][1] + new_guard_y == block_y):
            new_dir = (new_dir + 1) % len(dirs)
            bounce_limit -= 1
            if (new_guard_x, new_guard_y) in visited_cells_by_direction[new_dir]:
                return True
            if (new_guard_x, new_guard_y) in visited_cells_by_direction_during_test[new_dir]:
                return True
            visited_cells_by_direction_during_test[new_dir].add((new_guard_x, new_guard_y))
            continue
        new_guard_x += dirs[new_dir][0]
        new_guard_y += dirs[new_dir][1]
        if (new_guard_x, new_guard_y) in visited_cells_by_direction[new_dir]:
            return True
        if (new_guard_x, new_guard_y) in visited_cells_by_direction_during_test[new_dir]:
            return True
        visited_cells_by_direction_during_test[new_dir].add((new_guard_x, new_guard_y))


while guard_move():
    if 0 <= dirs[guard_dir][1] + guard_y < len(input):
        if 0 <= dirs[guard_dir][0] + guard_x < len(input[guard_y]):
            if not (guard_x + dirs[guard_dir][0], guard_y + dirs[guard_dir][1]) in visited_cells:
                if input[guard_y + dirs[guard_dir][1]][dirs[guard_dir][0] + guard_x] != '#':
                    if crossed_path() or rotate_would_meet_path():
                        possible_blocks.add((guard_x + dirs[guard_dir][0], guard_y + dirs[guard_dir][1]))
                        input[guard_y + dirs[guard_dir][1]][dirs[guard_dir][0] + guard_x] = "O"
    
    visited_cells.add((guard_x, guard_y))
    visited_cells_by_direction[guard_dir].add((guard_x, guard_y))

# for l in input:
#     for c in l:
#         print(c, end="")
#     print("")

a = len(visited_cells)
b = len(possible_blocks)

print(a, b)

