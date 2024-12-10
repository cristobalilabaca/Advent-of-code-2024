with open('input1.txt', 'r') as file:
    lines = file.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip('\n').split('   ')

left = []
right = {}

for line in lines:
    left.append(int(line[0]))
    right[int(line[1])] = right.get(int(line[1]), 0) + 1


dist = 0
for i in left:
    dist += i * right.get(i, 0)

print(dist)