# 1. 현재 위치에 퀸 배치 가능 여부 함수 선언
def check(x):
    # 1-1.
    for i in range(x):
        # 같은 열에 있거나 대각선 위치에 있는 경우 False 반환
        if queen[i] == queen[x] or abs(queen[x] - queen[i]) == x - i: return False
    # 1-3. 배치 가능 시 True 반환
    return True
# 2. dfs 함수 선언
def dfs(x):
    global ans
    # 2-1. 종료 조건 설정
    if x == n: ans += 1
    # 2-2.
    for i in range(n):
        # 열 설정
        queen[x] = i
        # 현재 위치에 퀸 배치 가능 시 dfs 실행
        if check(x):
            dfs(x + 1)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    queen = [0] * (n+1)
    ans = 0
    dfs(0)
    # 3. 결과 출력
    print(f'#{test_case} {ans}')