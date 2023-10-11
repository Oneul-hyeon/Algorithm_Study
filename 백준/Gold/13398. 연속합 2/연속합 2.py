import sys
input = sys.stdin.readline

def solution(n, array):
    # 1. 2차원 dp 생성
    dp = [[0 for _ in range(n)] for _ in range(2)]
    # 2. 초기값 설정
    dp[0][0], dp[1][0] = array[0], array[0]
    # 3.
    for i in range(1, n) :
        # 수를 제거하지 않는 경우
        dp[0][i] = max(dp[0][i-1] + array[i], array[i])
        # 수를 제거하는 경우
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + array[i])
    # 4. 결과 출력
    print(max(max(dp[0]), max(dp[1])))

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    solution(n, array)