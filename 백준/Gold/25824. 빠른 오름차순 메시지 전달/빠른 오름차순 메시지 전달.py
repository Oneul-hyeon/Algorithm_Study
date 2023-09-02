import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(student, group, time) :
    global ans
    # 1-1. 같은 그룹 내 다른 친구에게 전달
    another_student = student + 1 if student % 2 == 0 else student - 1
    time += graph[student][another_student]
    # 1-2. 종료 조건 설정
    if group == 6 :
        ans = min(ans, time)
        return
    # 1-3. 다음 그룹의 친구에게 전달
    backtracking(group * 2, group + 1, time + graph[another_student][group * 2])
    backtracking(group * 2 + 1, group + 1, time + graph[another_student][group * 2 + 1])

graph = [list(map(int, input().split(' '))) for _ in range(12)]
ans = float('inf')
# 2. 백트래킹 실행
backtracking(0, 1, 0)
backtracking(1, 1, 0)
# 3. 결과 출력
print(ans)