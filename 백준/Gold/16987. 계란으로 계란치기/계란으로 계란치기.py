import sys
input = sys.stdin.readline

# 1. 깨진 계란의 개수 체크 함수 선언
def check() :
    count = 0
    # 1-1.
    for i in range(n) :
        # 깨진 계란 개수 카운팅
        if eggs[i][0] <= 0 : count += 1
    # 1-2. 깨진 계란의 수 리턴
    return count

# 2. 백트래킹 함수 선언
def backtracking(idx) :
    global ans
    # 2-1. 종료 조건 설정
    if idx == n :
        # 최댓값 업데이트
        ans = max(ans, check())
        return
    # 2-2. 현재 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없을 경우
    if eggs[idx][0] <= 0 or check() == n - 1 :
        backtracking(idx + 1)
        return
    # 2-3.
    for i in range(n) :
        if i == idx : continue
        if eggs[i][0] > 0 :
            # 계란치기
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            # 백트래킹 함수 실행
            backtracking(idx + 1)
            # 계란 내구도 원상복구
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

n = int(input())
ans = 0
# 3. 계란 입력받기
eggs = [list(map(int, input().split())) for _ in range(n)]
# 4. 백트래킹 함수 실행
backtracking(0)
# 5. 결과 출력
print(ans)