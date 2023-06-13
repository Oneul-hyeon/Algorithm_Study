import sys
input = sys.stdin.readline

r, c, q = map(int, input().split())

# 1. 누적합 리스트 생성
prefix_sum = [[0] * (c+1)] + [([0] + list(map(int, input().split()))) for _ in range(r)]
# 2. 각 행과 열 처리를 통한 누적합 리스트 설정
for i in range(1, r+1) :
    for j in range(1, c+1) :
        prefix_sum[i][j] += prefix_sum[i][j-1]
for j in range(1, c+1) :
    for i in range(1, r+1) :
        prefix_sum[i][j] += prefix_sum[i-1][j]
# 3. 주어진 조건에 따른 구간합 구하기
for _ in range(q) :
    r1, c1, r2, c2 = map(int, input().split())
    summation = prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1]
    print(summation // ((r2-r1+1) * (c2-c1+1)))
