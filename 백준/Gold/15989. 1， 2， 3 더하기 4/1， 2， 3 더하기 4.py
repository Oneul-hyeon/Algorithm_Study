import sys
input = sys.stdin.readline

def solution(case):
    # 1. dp 생성
    dp = [1 for _ in range(10001)]
    # 2. 2를 더하는 경우
    for i in range(2, 10001) : dp[i] += dp[i-2]
    # 3. 3을 더하는 경우
    for i in range(3, 10001) : dp[i] += dp[i-3]
    # 4. 결과 출력
    for num in case :
        print(dp[num])

if __name__ == "__main__":
    T = int(input())
    case = [int(input()) for _ in range(T)]
    solution(case)