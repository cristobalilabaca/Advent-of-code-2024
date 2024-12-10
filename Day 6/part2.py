with open('input-test6.txt', 'r') as file:
    lines = file.readlines()

position = [0, 0]

for line in range(len(lines)):
    if '^' in lines[line]:
        position = [line, lines[line].index('^')]
    lines[line] = list(lines[line].strip('\n'))

loops = 0

while position[0] < len(lines) - 1 and position[0] > 0 and position[1] < len(lines[position[0]]) - 1 and position[1] > 0:
    if lines[position[0]][position[1]] == '>':
        if lines[position[0]][position[1] + 1] != '#':
            if lines[position[0]][position[1] + 1] == 'X':
                loops += 1
                for i in lines:
                    print(i)
                print()
            lines[position[0]][position[1]] = 'X'
            position[1] += 1
            lines[position[0]][position[1]] = '>'
        else:
            lines[position[0]][position[1]] = 'v'
    elif lines[position[0]][position[1]] == 'v':
        if lines[position[0] + 1][position[1]] != '#':
            if lines[position[0] + 1][position[1]] == 'X':
                loops += 1
                for i in lines:
                    print(i)
                print()
            lines[position[0]][position[1]] = 'X'
            position[0] += 1
            lines[position[0]][position[1]] = 'v'
        else:
            lines[position[0]][position[1]] = '<'
    elif lines[position[0]][position[1]] == '<':
        if lines[position[0]][position[1] - 1] != '#':
            if lines[position[0]][position[1] - 1] == 'X':
                loops += 1
                for i in lines:
                    print(i)
                print()
            lines[position[0]][position[1]] = 'X'
            position[1] -= 1
            lines[position[0]][position[1]] = '<'
        else:
            lines[position[0]][position[1]] = '^'
    elif lines[position[0]][position[1]] == '^':
        if lines[position[0] - 1][position[1]] != '#':
            if lines[position[0] - 1][position[1]] == 'X':
                loops += 1
                for i in lines:
                    print(i)
                print()
            lines[position[0]][position[1]] = 'X'
            position[0] -= 1
            lines[position[0]][position[1]] = '^'
        else:
            lines[position[0]][position[1]] = '>'

print(loops)
