with open('input2.txt', 'r') as file:
    lines = file.readlines()

for line in range(len(lines)):
    lines[line] = lines[line].strip('\n').split(' ')
    for i in range(len(lines[line])):
        lines[line][i] = int(lines[line][i])

safes = 0

for report in lines:
    sign = report[1] - report[0]
    if sign == 0:
        continue
    safe = True
    for level in range(len(report) - 1):
        if sign > 0 and report[level + 1] - report[level] <= 0:
            safe = False
            break
        elif sign < 0 and report[level + 1] - report[level] >= 0:
            safe = False
            break
        if abs(report[level + 1] - report[level]) > 3:
            safe = False
            break
    if safe:
        safes += 1

print(safes)
