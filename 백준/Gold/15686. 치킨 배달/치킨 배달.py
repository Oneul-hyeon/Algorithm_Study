import sys
from itertools import combinations
input = sys.stdin.readline

# 1. 도시의 치킨 거리 계산 함수 정의
def calculate_chicken_distance_of_city(store) :
    # 1-1. 각 집의 치킨 거리 계산 함수 정의
    def calculate_chicken_distance(x, y) :
        # 1-1-1. 최솟값 변수 정의
        min_dist = float("INF")
        # 1-1-2.
        for chicken_x, chicken_y in store :
            min_dist = min(min_dist, abs(x - chicken_x) + abs(y - chicken_y))
        # 1-1-3. 치킨 거리 반환
        return min_dist
    # 1-2. 도시의 치킨 거리 변수 정의
    chicken_distance_of_city = 0
    # 1-3.
    for x, y in home :
        # 도시의 치킨 거리 업데이트
        chicken_distance_of_city += calculate_chicken_distance(x, y)
    # 1-4. 도시의 치킨 거리 반환
    return chicken_distance_of_city

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 2. 집 리스트 생성
# 3. 치킨 집 리스트 생성
home, store = [], []
for x in range(n) :
    for y in range(n) :
        if graph[x][y] == 1 :
            home.append((x, y))
        elif graph[x][y] == 2 :
            store.append((x, y))
# 4. 출력 변수 정의
ans = float("INF")
# 5.
for combination in combinations(store, m) :
    # 5-1 도시의 치킨 거리의 최솟값 업데이트
    ans = min(ans, calculate_chicken_distance_of_city(combination))
# 6. 결과 출력
print(ans)