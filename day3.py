import re

with open("day3input.txt", 'r') as f:
    content = f.read()


pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

matches = re.findall(pattern, content)

print(matches)

total = 0
execute = True
for match in matches:
    # Extract numbers from the match
    if match == 'do()':
        execute = True
    elif match == "don't()":
        execute = False
    elif execute:
        numbers = re.findall(r"\d+", match)
        x, y = map(int, numbers)  
        total += x * y 
   

print("Sum of valid mul results:", total)
