import sys
input = sys.stdin.readline

n = int(input())
array1, array2 = list(map(int, input().split())), list(map(int, input().split()))
row1, row2 = [], []
row1_zero = row2_zero = 0

# 1. 1행과 2행의 0의 갯수 추출
# 2. 0이 제거된 1행과 2행 추출
for i in range(n) :
    if array1[i] == 0 : row1_zero += 1
    else : row1.append(array1[i])

    if array2[i] == 0 : row2_zero += 1
    else : row2.append(array2[i])
if row1_zero == n or row2_zero == n : print(0)
else :
    # 3. dp 생성
    dp = [[[0 for _ in range(row2_zero + 1)] for _ in range(row1_zero + 1)] for _ in range(n)]
    # 4. 초기값 설정
    dp[0][0][0] = row1[0] * row2[0]
    # 5.
    for i in range(1, n) :
        for x in range(row1_zero + 1) :
            if i-x < 0 or i-x >= len(row1) : continue
            for y in range(row2_zero + 1) :
                if i-y < 0 or i-y >= len(row2): continue
                # 5-1. 점화식에 따라 처리
                dp[i][x][y] = dp[i-1][x][y] + row1[i-x] * row2[i-y]
                if x-1 >= 0 : dp[i][x][y] = max(dp[i][x][y], dp[i-1][x-1][y])
                if y-1 >= 0 : dp[i][x][y] = max(dp[i][x][y], dp[i-1][x][y-1])
    # 6. 결과 출력
    print(dp[-1][-1][-1])