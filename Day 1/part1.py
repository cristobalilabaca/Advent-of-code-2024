with open('input1.txt', 'r') as file:
    lines = file.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip('\n').split('   ')

left = []
right = []

for line in lines:
    left.append(int(line[0]))
    right.append(int(line[1]))

left.sort()
right.sort()

dist = 0
for i in range(len(left)):
    dist += abs(left[i] - right[i])

print(dist)
