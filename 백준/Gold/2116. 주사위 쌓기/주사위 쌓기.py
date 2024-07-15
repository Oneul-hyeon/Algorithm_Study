import sys
input = sys.stdin.readline

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

# 1. 주사위 아랫면-윗변 대치 딕셔너리 생성
opposite_side = {0 : 5,
                 1 : 3,
                 2 : 4,
                 3 : 1,
                 4 : 2,
                 5 : 0}
# 2. 최댓값 변수 생성
ans = -int(1e9)
# 3.
for up_ in range(6) :
    summation = 0
    # 3-1. 첫 번째 주사위의 윗면 값 설정
    for idx, dice in enumerate(dices) :
        if idx == 0 : up = dice[up_]
        # 3-1-1. 현재 주사위의 아랫면 위치 추출
        down_ = dice.index(up)
        # 3-1-2. 현재 주사위의 윗면 위치 추출
        up_ = opposite_side[down_]
        # 3-1-3. 현재 주사위의 윗면 값 업데이트
        up = dice[up_]
        # 3-1-4. 현재 옆면의 합 업데이트
        for number in range(6, 0, -1) :
            if number not in (dice[down_], dice[up_]) :
                summation += number
                break
    # 3-2. 최댓값 업데이트
    ans = max(ans, summation)
# 4. 결과 출력
print(ans)