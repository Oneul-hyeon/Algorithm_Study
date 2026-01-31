import sys
from collections import deque
input = sys.stdin.readline

# 1. BFS 함수 정의
def BFS(info, n):
    # 1-1. 큐 생성 후 (시작 인덱스) 삽입
    queue = deque([0])
    visited = 1
    # 1-2.
    while queue:
        # 1-2-1. 인덱스, 방문 여부 추출
        index = queue.popleft()
        # 1-2-2.
        for _next in range(1, n+2):
            # 다음 위치를 방문하지 않은 경우
            if not visited & (1<<_next):
                # 다음 위치에 갈 수 있는 경우
                if abs(info[index][0] - info[_next][0]) + abs(info[index][1] - info[_next][1]) <= 1000:
                    # 다음 위치가 페스티벌이라면 "happy" 반환
                    if _next == n+1:
                        return "happy"
                    # 큐에 (다음 인덱스, 방문 여부) 삽입
                    visited |= (1<<_next)
                    queue.append(_next)
    # 1-3. "sad" 반환
    return "sad"
# 2.
for _ in range(int(input())):
    n = int(input())
    # 2-1. 좌표 리스트 입력
    info = [list(map(int, input().split())) for _ in range(n+2)]
    # 2-2. 결과 출력
    print(BFS(info, n))