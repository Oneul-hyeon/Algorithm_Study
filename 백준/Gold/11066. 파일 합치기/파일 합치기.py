import sys
input = sys.stdin.readline

def solution(t) :
    for _ in range(t) :
        k = int(input())
        array = [0] + list(map(int, input().split()))
        # 1. 누적합 리스트 생성
        for i in range(2, len(array)) :
            array[i] += array[i-1]
        # 2. DP 생성
        dp = [[0 for _ in range(k + 1)] for _ in range(k + 1)]
        # 3.
        for j in range(2, k + 1) :
            for i in range(1, k - j + 2) :
                # 점화식에 따라 처리
                dp[i][i + j - 1] = min([dp[i][i + x] + dp[i + x + 1][i + j - 1] for x in range(j - 1)]) + array[i + j - 1] - array[i - 1]
        # 4. 결과 출력
        print(dp[1][k])
        
if __name__ == "__main__" :
    t = int(input())
    solution(t)