import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

# 1. 뱀과 사다리 정보가 담긴 리스트 생성
array = [0] * 101
for _ in range(n+m) :
    u, v = map(int, input().split())
    array[u] = v
# 2. 방문 여부 리스트 생성
visited = [False] * 101
visited[1] = True
# 3. 큐에 (1, 0) 삽입
queue = deque([])
queue.append((1, 0))
# 4.
while queue :
    # 5. 큐에서 (현재 위치, 거리) 뽑기
    now, d = queue.popleft()
    # 6. 종료 조건 설정
    if now == 100 :
        print(d)
        break
    # 7.
    for i in range(1, 7) :
        # 8. 다음 위치, 거리 업데이트
        next, nd = now + i, d + 1
        # 9. 위치가 100을 넘어가거나 방문한 인덱스일 경우 건너뛰기
        if next > 100 or visited[next] : continue
        visited[next] = True
        # 10. 1에서 만든 리스트에 다음 위치 인덱스의 값이 있을 경우
        if array[next] : queue.append((array[next], nd))
        else : queue.append((next, nd))