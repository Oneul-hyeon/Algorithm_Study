import sys
input = sys.stdin.readline

n = int(input())
# 1. 첫 번째 줄 먼저 입력받기
max_ans = list(map(int, input().split()))
min_ans = max_ans[:]
# 2.
for _ in range(n-1) :
    # 2-1. 한 라인 입력받기
    max_dp = list(map(int, input().split()))
    min_dp = max_dp[:]
    # 2-2. 해당 라인의 인덱스 별 최대, 최소 점수 구하기
    max_dp[0] += max(max_ans[0:2])
    max_dp[1] += max(max_ans[0:3])
    max_dp[2] += max(max_ans[1:3])

    min_dp[0] += min(min_ans[0:2])
    min_dp[1] += min(min_ans[0:3])
    min_dp[2] += min(min_ans[1:3])

    # 2-3. DP 배열 값 복사
    max_ans = max_dp[:]
    min_ans = min_dp[:]
# 3. 결과 출력
print(f'{max(max_ans)} {min(min_ans)}')