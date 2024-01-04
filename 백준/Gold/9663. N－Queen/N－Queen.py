import sys
input = sys.stdin.readline

# 1. 배치 가능 여부 함수 정의
def check(x) :
    # 1-1.
    for i in range(x) :
        # 같은 열에 있거나 대각선에 위치할 경우 False 반환
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i : return False
    # 1-2. True 반환
    return True
# 2. 백트래킹 함수 정의
def dfs(x) :
    global ans
    # 2-1. 종료 조건 설정
    if x == n :
        ans += 1
        return
    # 2-2.
    for i in range(n) :
        queen[x] = i
        # 2-2-1. 배치 가능할 경우 백트래킹 실행
        if check(x) : dfs(x+1)

ans = 0
n = int(input())
# 3. queen 리스트 생성
queen = [0] * n
# 4. 백트래킹 함수 실행
dfs(0)
# 5. 결과 출력
print(ans)