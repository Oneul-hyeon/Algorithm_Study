import sys
input = sys.stdin.readline

# 1. 소수 판별 함수 정의
def check(num) :
    num = int(num)
    # 1-1.
    for i in range(2, int(num ** 0.5) + 1) :
        # 나누어질 경우 False 반환
        if num % i == 0 : return False
    # 1-2. True 반환
    return True
# 2. 백트래킹 함수 정의
def backtracking(l, num) :
    # 2-1. 종료 조건 설정
    if l == n + 1 :
        # 출력 리스트에 해당 수 삽입
        ans.append(num)
        return
    # 2-2.
    for i in range(1, 10) :
        # 2-2-1. 한 자리 수 탐색 시 1 제외
        if l == 1 and i in [0, 1] : continue
        # 2-2-2. 소수일 경우 백트래킹 실행
        next = num + str(i)
        if check(next) : backtracking(l+1, next)

n = int(input())
# 3. 출력 리스트 생성
ans = []
# 4. 백트래킹 실행
backtracking(1, '')
# 5.
for num in sorted(ans) : print(num) # 결과 출력