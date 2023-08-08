import sys
input = sys.stdin.readline

n, c, w = map(int, input().split())
trees = [int(input()) for _ in range(n)]
# 1. 최댓값 변수 선언
ans = -sys.maxsize
# 2.
for l in range(1, max(trees) + 1) :
    # 2-1. 자를 수 있는 나무 개수 세기
    k = 0
    profit = 0
    for tree in trees :
        k = tree // l
        # 2-2. 이득 계산
        profit += max(0, k * l * w - k * c if tree % l != 0 else k * l * w - (k-1) * c)
    # 2-3. 최댓값 갱신
    ans = max(ans, profit)
# 3. 결과 출력
print(ans)