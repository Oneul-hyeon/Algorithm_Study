import sys
from collections import deque
input = sys.stdin.readline

# 1. 익지 않은 토마토 체크 함수 정의
def check() -> bool :
    # 1-1.
    for h in range(H):
        for n in range(N):
            for m in range(M):
                # 1-1-1. 익지 않은 토마토가 있는 경우 True 반환
                if box[h][n][m]==0 : return True
    # 1-2. 익지 않은 토마토가 없으므로 False 반환
    return False

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 2. 익지 않은 토마토가 있는 경우
if check():
    # 2-1. 큐 생성 후 익은 토마토 인덱스 삽입
    queue = deque([(h, n, m) for h in range(H) for n in range(N) for m in range(M) if box[h][n][m] == 1])
    # 2-2.
    while queue:
        # 2-2-1. 익은 토마토 위치 인덱스 반환
        h, n, m = queue.popleft()
        # 2-2-2.
        for dir_h, dir_n, dir_m in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)]:
            # 다음 위치 설정
            nh, nn, nm = h+dir_h, n+dir_n, m+dir_m
            # 예외 처리
            if nh < 0 or nh >= H or nn < 0 or nn >= N or nm < 0 or nm >= M : continue
            # 익지 않은 토마토인 경우
            if box[nh][nn][nm]==0:
                # 최소 일자 업데이트
                box[nh][nn][nm] = box[h][n][m]+1
                # 큐에 다음 위치 인덱스 삽입
                queue.append((nh, nn, nm))
    # 2-3. 익지 않은 토마토가 있는 경우 -1 출력
    if check():
        print(-1)
    # 2-4. 최소 날짜 출력
    else :
        print(max([box[h][n][m] for h in range(H) for n in range(N) for m in range(M)]) - 1)
# 3. 모든 토마토가 익어 있는 경우 0 출력
else :
    print(0)