import sys
input = sys.stdin.readline

line = input().split('-')
result = 0
for line2 in line[0].split('+') :
    result += int(line2)

for line2 in line[1:]:
    for line3 in line2.split('+'):
        result -= int(line3)
print(result)