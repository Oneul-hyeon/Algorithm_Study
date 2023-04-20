import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# 1. 큐에 n만큼 입력받기
queue = [input().rstrip() for _ in range(n)]
queue = deque(queue)
answer = []
# 2. 이후 입력부터 하나씩 비교
for _ in range(n) :
    out = input().rstrip()
    # 2-1. 큐의 첫 번째 값이 별도의 리스트 안에 있다면 popleft
    while queue[0] in answer :
        queue.popleft()
    # 2-2. 입력이 큐의 첫 번째 값과 일치하다면 popleft
    if  out == queue[0]:
        queue.popleft()
    # 2-3. 입력이 큐의 첫 번째 값과 일치하지 않다면 별도의 리스트에 저장
    elif queue[0] != out : answer.append(out)
# 3. 리스트의 길이 출력
print(len(answer))