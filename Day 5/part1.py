from collections import defaultdict

with open('input5.txt', 'r') as file:
  lines = file.readlines()

ordering_rules = defaultdict(list)
updates = []

rules = True

for line in range(len(lines)):
  lines[line] = lines[line].strip('\n')

  if lines[line] == '':
    rules = False
  elif rules:
    ordering_rules[lines[line].split('|')[1]].append(lines[line].split('|')[0])
  else:
    updates.append(lines[line].split(','))

middle_page = 0

for update in updates:
  correct = True
  for page in range(len(update)):
    for i in range(page + 1, len(update)):
      if update[i] in ordering_rules[update[page]]:
        correct = False
        break
  if correct:
    middle_page += int(update[len(update) // 2])

print(middle_page)