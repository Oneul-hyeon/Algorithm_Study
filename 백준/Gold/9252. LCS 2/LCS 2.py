import sys
input = sys.stdin.readline

def solution(s1, s2) :
    l1, l2 = len(s1), len(s2)
    # 1. DP 생성
    dp = [[[0, ''] for _ in range(l2)] for _ in range(l1)]
    # 2.
    for i in range(1, l1) :
        for j in range(1, l2) :
            # 2-1. 두 문자가 같을 경우
            if s1[i] == s2[j] :
                # 점화식에 따라 처리
                dp[i][j][0] = dp[i-1][j-1][0] + 1
                # 문자 추가
                dp[i][j][1] = dp[i-1][j-1][1] + s1[i]
            # 2-2. 두 문자가 다른 경우
            else :
                # 점화식에 따라 처리
                dp[i][j] = dp[i-1][j] if dp[i-1][j][0] > dp[i][j-1][0] else dp[i][j-1]
    # 3. 결과 출력
    print(f'{dp[-1][-1][0]}\n{dp[-1][-1][1]}')
if __name__ == "__main__" :
    s1, s2 = " " + input().rstrip(), " " + input().rstrip()
    solution(s1, s2)