import sys
input = sys.stdin.readline

def solution(n) :
    # 1. 최댓값, 최솟값 DP 생성
    INF = int(1e9)
    max_dp, min_dp = [-INF for _ in range(n+1)], [INF for _ in range(n+1)]
    max_dp[0], min_dp[0], = 0, 0
    # 2. 피보나치 변수 생성
    now, pre = [2, 1], [1, 1]
    # 3.
    while now[0] <= n :
        p, c = now[0], now[1]
        for i in range(p, n+1) :
            # 3-1. 최댓값 업데이트
            if max_dp[i - p] != -INF or i % p == 0 : max_dp[i] = max(max_dp[i], max_dp[i-p] + c)
            # 3-2. 최솟값 업데이트
            if min_dp[i - p] != INF or i % p == 0 : min_dp[i] = min(min_dp[i], min_dp[i-p] + c)
        # 3-3. 피보나치 변수 업데이트
        now, pre = [a + b for a, b in zip(now[:], pre[:])], now[:]
    # 4. 결과 출력
    print(f'{min_dp[-1]} {max_dp[-1]}')

if __name__ == "__main__" :
    n = int(input())
    solution(n)