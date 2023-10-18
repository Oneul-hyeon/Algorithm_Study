import sys
input = sys.stdin.readline

def solution() :
    t, w = map(int, input().split())
    array = [0] + [int(input()) for _ in range(t)]
    # 1. dp 생성
    dp = [[0 for _ in range(w+1)] for _ in range(t+1)]
    # 2.
    for i in range(1, t+1) :
        # 2-1. 움직이지 않는 경우
        # 1번 나무의 경우
        if array[i] == 1 : dp[i][0] = dp[i-1][0] + 1
        # 2번 나무의 경우
        else : dp[i][0] = dp[i-1][0]
        # 2-2.
        for j in range(1, w+1) :
            # 현재 위치가 1번이고, 1번 나무에서 자두가 떨어질 경우 & 현재 위치가 2번이고, 2번 나무에서 자두가 떨어질 경우
            if (j % 2 == 0 and array[i] == 1) or (j % 2 != 0 and array[i] == 2) : dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            # 자두를 먹지 못하는 경우
            else : dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
    # 3. 결과 출력
    print(max(dp[-1][:]))
    
if __name__ == "__main__":
    solution()