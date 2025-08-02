import sys
from typing import Annotated
from collections import deque

input = sys.stdin.readline

# 1. 재귀 함수 정의
def checker() -> Annotated[int, "0(클리어 불가) or 1(클리어 가능)"]:
    # 1-1. 큐 생성
    queue = deque([])
    # 1-2. 큐에 초기 위치 삽입
    queue.append((0, 0, 0))
    # 1-3. 방문 여부 리스트 생성 후 현재 위치 방문 처리
    visited = [[False] * n for _ in range(2)]
    visited[0][0]=True
    # 1-4.
    while queue:
        # 1-4-1. 큐에서 값 추출
        line, position, time = queue.popleft()
        # 1-4-2.
        for jump, dist in [(0, 1), (0, -1), (1, k)] :
            # 다음 줄, 위치 선정
            next_line, next_position = (line+jump)%2, position+dist
            # 종료 조건 설정
            if next_position >= n:
                return 1
            # 예외 처리
            if next_position <= time or not board[next_line][next_position] or visited[next_line][next_position] :
                continue
            # 현재 위치 방문 처리
            visited[next_line][next_position]=True
            # 큐에 (다음 줄, 다음 위치, 시간) 삽입
            queue.append((next_line, next_position, time+1))
    # 게임 클리어를 못 하는 경우
    return 0

n, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(2)]

# 2. 게임 클리어 여부 출력
print(checker())