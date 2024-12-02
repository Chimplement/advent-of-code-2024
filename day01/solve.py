input = open(0).read();

all = map(int, input.split());
left = []
right = []

for i, n in enumerate(all):
    if (i % 2 == 0):
        left.append(n)
    else:
        right.append(n)

left.sort()
right.sort()

total_distance = 0
similarity_score = 0

for n1, n2 in zip(left, right):
    total_distance += abs(n1 - n2)
    similarity_score += n1 * right.count(n1)

print(total_distance, similarity_score)