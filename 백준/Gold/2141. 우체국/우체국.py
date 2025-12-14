import sys
input = sys.stdin.readline

N = int(input())
# 1. 마을 정보 입력
info = sorted([list(map(int, input().split())) for _ in range(N)])
# 2. 중앙값 추출
X = sum(list(zip(*info))[1])
mid = X//2 if X%2 == 0 else (X+1)//2
# 3. 중앙값에 해당하는 위치 출력
for idx, cnt in info:
    mid -= cnt
    if mid <= 0:
        print(idx)
        exit()