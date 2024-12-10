import re

with open('input4.txt', 'r') as file:
    lines = file.readlines()

mas_count = 0

for line in range(len(lines)):
    lines[line] = list(lines[line].strip('\n'))

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        if lines[i][j] == 'A':
            if lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S':
                if lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S':
                    mas_count += 1
                elif lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M':
                    mas_count += 1
            elif lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M':
                if lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S':
                    mas_count += 1
                elif lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M':
                    mas_count += 1

print(mas_count)
