import re

with open('input4.txt', 'r') as file:
    lines = file.readlines()

xmas_count = 0

for line in range(len(lines)):
    # horizontal search
    xmas_count += len(re.findall('XMAS', lines[line]))
    xmas_count += len(re.findall('SAMX', lines[line]))

    lines[line] = list(lines[line].strip('\n'))

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            if i < len(lines) - 3:
                # down search
                if lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
                    xmas_count += 1
                
                # down right search
                if j < len(lines[i]) - 3:
                    if lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
                        xmas_count += 1

                # down left search
                if j > 2:
                    if lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
                        xmas_count += 1

            if i > 2:
                # up search
                if lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
                    xmas_count += 1

                # up right search
                if j < len(lines[i]) - 3:
                    if lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
                        xmas_count += 1

                # up left search
                if j > 2:
                    if lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
                        xmas_count += 1

print(xmas_count)
