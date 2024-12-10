import re

with open('input3.txt', 'r') as file:
  lines = file.readlines()

for line in range(len(lines)):
  lines[line] = lines[line].strip('\n')

mul_sum = 0
multiplying = True

for line in lines:
  muls = re.findall(r'(?:mul\(\d{1,3},\d{1,3}\)|(?:do|don\'t)\(\))', line)
  for mul in muls:
    if mul == 'do()':
      multiplying = True
    elif mul == "don't()":
      multiplying = False
    elif multiplying:
      clean_mul = mul.strip('mul(').strip(')')
      mul_parts = clean_mul.split(',')
      mul_sum += int(mul_parts[0]) * int(mul_parts[1])

print(mul_sum)