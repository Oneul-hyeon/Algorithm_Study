import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(now, hp, count) :
    global ans
    # 1-1. 마실 수 있는 민트 초코 우유 개수
    if count > ans :
        if abs(now[0] - home[0]) + abs(now[1] - home[1]) <= hp : ans = max(ans, count)
    # 1-2.
    for i in range(len(mint_choco)) :
        # 현재 위치에서 다음 위치까지의 거리 계산
        distance = abs(now[0] - mint_choco[i][0]) + abs(now[1] - mint_choco[i][1])
        # 체력이 거리보다 클 경우
        if hp >= distance :
            # 민트 초코 우유 리스트에서 다음 위치 제거
            next = mint_choco.pop(i)
            # 백트래킹 실행
            backtracking(next, hp - distance + h, count + 1)
            # 민트 초코 우유 리스트에서 다음 위치 삽입
            mint_choco.insert(i, next)

n, m, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 2.
mint_choco = []
for i in range(n) :
    for j in range(n) :
        # 2-1. 민트 초코 우유 위치 리스트
        if graph[i][j] == 2 : mint_choco.append((i,j))
        # 2-2. 진우의 집 위치
        elif graph[i][j] == 1 : home = (i, j)
# 3. 백트래킹 함수 실행
backtracking(home, m, 0)
# 4. 결과 출력
print(ans)