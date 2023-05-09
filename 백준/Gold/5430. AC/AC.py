import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case) :
    command = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    queue = deque(arr)
    if command.count('D') > n : print('error')
    elif n == 0 and 'D' in command: print('error')
    elif n == 0 or n == command.count('D'): print('[]')
    else:
        flag = 0
        for x in range(len(command)) :
            if command[x] == 'R' :
                flag+=1
            elif command[x] == 'D' :
                if flag%2 != 0 :
                    queue.pop()
                else :
                    queue.popleft()
        if flag%2 != 0 :
            queue.reverse()
        print('[' + ','.join(queue) + ']')