import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

# 1. BFS 함수 정의
def bfs():
    # 1-1. 큐 생성 후 (scv 체력, 초기 공격 횟수) 정보 삽입
    queue = deque([(scv_hp, 0)])
    # 1-2.
    while queue:
        # 1-2-1. 체력, 공격 횟수 반환
        hp, cnt = queue.popleft()
        # 1-2-2.
        for power in powers:
            # 공격 후 잔여 HP 계산
            x, y, z = [scv_hp-p if scv_hp-p > 0 else 0 for scv_hp, p in zip(hp, power)]
            # 모든 SCV가 파괴된 경우
            if x == y == z == 0 :
                # 최소 공격 횟수 반환
                return cnt + 1
            # 잔여 HP가 구해진 적이 없는 경우
            if not checked[x][y][z]:
                # 잔여 HP 체크 처리
                checked[x][y][z] = True
                # 큐에 (잔여 HP, 공격 횟수) 삽입
                queue.append(([x, y, z], cnt+1))

N = int(input())
scv_hp = list(map(int, input().split())) + [0 for _ in range(3-N)]

# 2. SCV HP 계산 여부 리스트 생성 및 초기 설정
checked = [
    [
        [False for _ in range(61)]
        for _ in range(61)
    ]
    for _ in range(61)
]
checked[scv_hp[0]][scv_hp[1]][scv_hp[2]] = True
# 3. 뮤탈리스크 공격에 따른 공격력 순열 생성
powers = list(permutations((9, 3, 1)))
# 4. 최소 공격 횟수 출력
print(bfs())