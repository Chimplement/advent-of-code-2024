input = open(0).read().splitlines();

def can_read_xmas(l, x, y, dir_x, dir_y) -> bool:
    for i,c in enumerate("XMAS"):
        if not 0<=y+dir_y*i<len(l):
            return False
        if not 0<=x+dir_x*i<len(l[y]):
            return False
        if l[y+dir_y*i][x+dir_x*i] != c:
            return False
    return True

def count_xmas_starting_at(l: list[str], x, y) -> int:
    if (l[y][x] != 'X'):
        return 0
    return (can_read_xmas(l, x, y, 1, 0) + can_read_xmas(l, x, y, 1, 1) + can_read_xmas(l, x, y, 0, 1) +
            can_read_xmas(l, x, y, -1, 1) + can_read_xmas(l, x, y, -1, 0) + can_read_xmas(l, x, y, -1, -1) +
            can_read_xmas(l, x, y, 0, -1) + can_read_xmas(l, x, y, 1, -1))

def is_center_of_mas(l, x, y, dir_x, dir_y) -> bool:
    if not 1<=y<len(l)-1:
        return False
    if not 1<=x<len(l[y])-1:
        return False
    
    return l[y][x] == 'A' and l[y+dir_x][x+dir_y] == "M" and l[y-dir_x][x-dir_y] == "S"


def is_center_of_x_mas(l: list[str], x, y) -> bool:
    if (l[y][x] != 'A'):
        return False
    
    if is_center_of_mas(l, x, y, -1, -1):
        if is_center_of_mas(l, x, y, 1, -1):
            return True
        if is_center_of_mas(l, x, y, -1, 1):
            return True
    
    if is_center_of_mas(l, x, y, 1, 1):
        if is_center_of_mas(l, x, y, 1, -1):
            return True
        if is_center_of_mas(l, x, y, -1, 1):
            return True
    
    return False

a = 0
b = 0

for y in range(len(input)):
    for x in range(len(input[y])):
        a += count_xmas_starting_at(input, x, y)
        b += is_center_of_x_mas(input, x, y)

print(a, b)