import sys
input = sys.stdin.readline

n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]

# 1. 끝나는 시간이 가장 늦은 일 순으로 정렬
works.sort(key = lambda x : [-x[1], -x[0]])
# 2. 출력 변수 정의
ans = works[0][1] - works[0][0]
# 3.
for t, s in works[1:] :
    # 3-1. 일 시작 가능 시간이 해당 작업 마감 시간보다 작을 경우
    if ans > s : ans = s - t
    # 3-2. 그 외의 경우
    else : ans -= t
# 4. 결과 출력
print(ans if ans >= 0 else -1)