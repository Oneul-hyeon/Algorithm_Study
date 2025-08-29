import sys
from collections import deque
input = sys.stdin.readline

# 1. bfs 함수 정의
def bfs():
    # 1-1. 큐 생성 후 (시작 위치, 초기 시간) 삽입
    queue = deque([(N, 0)])
    # 1-2.
    while queue:
        # 1-2-1. 인덱스 및 시간 정보 추출
        idx, time = queue.popleft()
        # 1-2-2.
        for nidx in [idx-1, idx+1, 2*idx]:
            # 예외 처리
            if nidx < 0 or nidx > 100_000 : continue
            # 다음 위치에 방문하지 않은 경우
            if backtracking_list[nidx] == -1:
                # 역추적 리스트의 다음 위치에 현재 위치 정보 삽입
                backtracking_list[nidx] = idx
                # 목표 지점에 도착한 경우
                if nidx == K :
                    # 최단 시간 결과 반환
                    return time+1
                # 이외의 경우
                else :
                    # 큐에 다음 위치 정보 삽입
                    queue.append((nidx, time+1))

N, K = map(int, input().split())
if N == K : print(f"0\n{N}")
else :
    # 2. 역추적 리스트 생성
    backtracking_list = [-1 for _ in range(100_001)]
    # 3. bfs 함수를 통해 최단 시간 추출
    min_time = bfs()
    # 4. 최단 경로 리스트 생성
    min_route = [str(K)]
    # 5.
    idx = K
    while idx != N:
        # 5-1. 다음 경로 설정
        idx = backtracking_list[idx]
        # 5-2. 경로 추적
        min_route.append(str(idx))
    # 6. 결과 출력
    print(f"{min_time}\n{' '.join(min_route[::-1])}")