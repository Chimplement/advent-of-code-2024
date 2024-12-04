import re

input = open(0).read();

enabled = True
a = 0
b = 0

for instruction in re.findall(r"mul\(\d+.\d+\)|do\(\)|don't\(\)", input):
    if instruction == "do()":
        enabled = True
        continue
    elif instruction == "don't()":
        enabled = False
        continue

    mul = instruction[4:-1]
    mul = list(map(int, mul.split(",")))
    if len(mul) == 2:
        res = mul[0] * mul[1]
        a += res
        if enabled:
            b += res

print(a, b)