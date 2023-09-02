import sys, math
input = sys.stdin.readline

n, l = map(int, input().split())
# 1. 웅덩이 위치 정렬하기
info = sorted([list(map(int, input().split())) for _ in range(n)])
# 2. 널빤지 필요 수 변수 정의
ans = 0
# 3. 널빤지의 마지막 위치 정의
now_e = 0
# 4.
for i in range(n) :
    s, e = info[i]
    # 4-1. 시작 위치가 이미 덮여있을 경우
    if now_e >= s : s = now_e
    # 4-2. 널빤지 개수 카운트
    cnt = math.ceil((e - s) / l)
    ans += cnt
    # 4-3. 널빤지의 마지막 위치 재정의
    now_e = s + l * cnt
# 5. 결과 출력
print(ans)