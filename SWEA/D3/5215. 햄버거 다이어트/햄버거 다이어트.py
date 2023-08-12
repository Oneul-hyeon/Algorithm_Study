# 1. 백트래킹 함수 정의
def backtracking(idx, score, cal) :
    global ans
    # 1-1. 종료 조건 설정
    if idx == n : return
    # 1-2. 현재 재료를 합친 점수와 칼로리 계산
    new_score, new_cal = score + ingredients[idx][0], cal + ingredients[idx][1]
    # 1-3. 최댓값 업데이트
    if new_cal <= l : ans = max(ans, new_score)
    # 1-4. 백트래킹 함수 실행
    # 현재 재료를 넣지 않는 경우
    backtracking(idx+1, score, cal)
    # 현재 재료를 넣는 경우
    backtracking(idx+1, new_score, new_cal)

t = int(input())
for test_case in range(1, t+1) :
    n, l = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    # 2. 백트래킹 함수 실행
    backtracking(0, 0, 0)
    # 3. 결과 출력
    print(f'#{test_case} {ans}')