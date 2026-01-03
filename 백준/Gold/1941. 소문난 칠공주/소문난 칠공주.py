import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 1. 인접 여부 체크 함수 생성
def is_connected(combination):
    # 1-1. 인접 체크용 딕셔너리 생성
    checked = {(x, y): False for x, y in combination}
    # 1-2. 샘플 인덱스 추출
    x, y = combination[0]
    # 1-3. 큐 생성 후 샘플 인덱스 삽입
    queue = deque([(x, y)])
    # 1-4. 현재 위치 방문 처리
    checked[(x, y)] = True
    # 1-5.
    while queue:
        # 1-5-1. 큐에서 인덱스 추출
        x, y = queue.popleft()
        # 1-5-2.
        for dir_x, dir_y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # 다음 위치 설정
            nx, ny = x+dir_x, y+dir_y
            # 다음 위치 인덱스가 딕셔너리 내에 있는 경우 체크
            if (nx, ny) in checked and not checked[(nx, ny)]:
                checked[(nx, ny)] = True
                queue.append((nx, ny))

    # 1-3. 모두 인접한 경우 True, 인접하지 않은 경우 False 반환
    if False in checked.values(): return False
    else: return True

# 2. 칠공주 결성 여부 체크 함수 생성
def is_formation(combination):
    # 2-1. 칠공주 결성 체크용 딕셔너리 생성
    count = {"Y":0, "S":0}
    # 2-2. 소속 체크
    for x, y in combination: count[graph[x][y]] += 1
    # 2-3. 이다솜파가 더 많은 경우 True, 그렇지 않은 경우 False 반환
    if count["S"] > count["Y"]: return True
    else: return False

size = 5
graph = [list(input().strip()) for _ in range(size)]

# 2. 카운트 변수 생성
ans = 0
# 3.
for combination in combinations([(x, y) for x in range(size) for y in range(size)], 7):
    # 3-1. 해당 조합이 인접하면서 칠공주 결성이 가능한 경우 카운팅
    if is_connected(combination) and is_formation(combination): ans += 1
# 4. 모든 경우의 수 출력하기
print(ans)