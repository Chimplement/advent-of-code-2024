input = [l.split(":") for l in open(0).read().splitlines()];
for l in input:
    l[0] = int(l[0])
    l[1] = l[1].lstrip(" ")

operations = [int.__add__, int.__mul__, lambda a,b: int(str(a) + str(b))]

def check(l: list[int, str]) -> bool:
    spaces = [i for i,c in enumerate(l[1]) if c == " "]
    split_on_spaces = list(map(int, l[1].split(" ")))
    i = 0
    while True:
        result = split_on_spaces[0]
        b = ("0" * 32 + bin(i).lstrip("0b"))[::-1]
        for j in range(len(spaces)):
            result = operations[int(b[j])](result, split_on_spaces[j + 1])
        if result == l[0]:
            return True
        b = bin(i).lstrip("0b")
        if (len(b) == len(spaces) and b == "1" * len(b)):
            break
        i += 1
    return False

def trin(a: int) -> str:
    s = ""
    while a > 0:
        s = str(a % 3) + s
        a = int(a / 3)
    return s

def checkb(l: list[int, str]) -> bool:
    spaces = [i for i,c in enumerate(l[1]) if c == " "]
    split_on_spaces = list(map(int, l[1].split(" ")))
    i = 0
    while True:
        result = split_on_spaces[0]
        b = ("0" * 64 + trin(i))[::-1]
        for j in range(len(spaces)):
            result = operations[int(b[j])](result, split_on_spaces[j + 1])
        if result == l[0]:
            return True
        b = trin(i)
        if (len(b) == len(spaces) and b == "2" * len(b)):
            break
        i += 1
    return False

a = 0
b = 0


for l in input:
    if check(l):
        a += l[0]
    if checkb(l):
        b += l[0]

print(a, b)

