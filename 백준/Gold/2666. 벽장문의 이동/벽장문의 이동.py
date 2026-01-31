import sys
input = sys.stdin.readline

# 1. DFS 함수 정의
def DFS(num, space1, space2, cnt):
    global ans

    # 1-1. 종료 조건 설정
    # 1-1-1. 모든 벽장을 연 경우
    if num == M:
        # 최소 이동 횟수 업데이트
        ans = min(ans, cnt)
        return
    # 1-2. 열어야 하는 벽장 인덱스 추출
    target = sequence[num]
    # 1-3. 타겟을 하는 벽장의 양 옆에 빈 공간이 있는 경우
    if (l:=min(space1, space2)) < target < (r:=max(space1, space2)):
        # 1-3-1. 벽장을 왼쪽으로 이동
        DFS(num+1, target, r, cnt+target-l)
        # 1-3-2. 벽장을 오른쪽으로 이동
        DFS(num+1, l, target, cnt+r-target)
    # 1-4. 타겟을 하는 벽장의 빈 공간이 한 쪽으로 쏠려 있는 경우
    else:
        if abs(target-space1) < abs(target-space2):
            DFS(num+1, target, space2, cnt+abs(target-space1))
        else:
            DFS(num + 1, space1, target, cnt + abs(target - space2))

N = int(input())
space1, space2 = sorted(map(int, input().split()))
M = int(input())
sequence = [int(input()) for _ in range(M)]

# 2. 정답 변수 초기화
ans = int(1e9)
# 3. DFS 실행
DFS(0, space1, space2, 0)
# 4. 결과 출력
print(ans)