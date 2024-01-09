import sys
input = sys.stdin.readline

string = list(input().rstrip())
boom = list(input().rstrip())
l = len(boom)
stack = []
for s in string :
    stack.append(s)
    if stack[-l:] == boom :
        for _ in range(l) : stack.pop()
print("FRULA" if not stack else ''.join(stack))