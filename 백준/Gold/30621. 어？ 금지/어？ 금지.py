import sys
from bisect import bisect_left
input = sys.stdin.readline

def solution(n, time, blank, cost) :
    # 1. 시각, 혼란값 dp 생성
    dp = [0 for _ in range(n+1)]
    # 2.
    for i in range(1, n+1) :
        t, b, c = time[i], blank[i], cost[i]
        # 2-1. t - b초 직전의 초에 해당하는 인덱스 값 찾기
        idx = bisect_left(time, t-b) - 1
        # 2-2. 점화식에 따라 최대 혼란값 생성
        dp[i] = max(dp[i-1], dp[idx] + c)
    # 3. 결과 출력
    print(dp[-1])
    
if __name__ == "__main__" :
    n = int(input())
    time = [0] + list(map(int, input().split()))
    blank = [0] + list(map(int, input().split()))
    cost = [0] + list(map(int, input().split()))
    solution(n, time, blank, cost)