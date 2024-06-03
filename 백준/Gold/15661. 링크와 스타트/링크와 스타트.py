import sys
from itertools import combinations
input = sys.stdin.readline

# 1. 팀 능력치 계산 함수 정의
def calculate_power(team) :
    team_power = 0
    # 1-1.
    for i in range(len(team)) :
        for j in range(i+1, len(team)) :
            p1, p2 = team[i], team[j]
            # 팀 능력치 계산
            team_power += power[p1][p2] + power[p2][p1]
    # 1-2. 계산된 능력치 반환
    return team_power

ans = int(1e9)
n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]
# 2.
for cnt in range(1, n//2 + 1) :
    # 2-1. 조합 구하기
    combination = combinations(range(n), cnt)
    # 2-2.
    for comb in combination :
        # 2-2-1. 해당 조합의 능력치 산정
        start_team = comb
        link_team = list(set(range(n)) - set(start_team))
        start_team_power = calculate_power(start_team)
        link_team_power = calculate_power(link_team)
        # 2-2-2. 능력치 차이의 최솟값 업데이트
        ans = min(ans, abs(start_team_power - link_team_power))
# 4. 결과 출력
print(ans)