import sys
input = sys.stdin.readline

string = input().rstrip()
stack = []

for s in string :
    stack.append(s)
    if ''.join(stack[-4:]) == 'PPAP' :
        for _ in range(3) : stack.pop()

print('PPAP') if ''.join(stack) == 'P' else print('NP')