import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    # 1. 신입사원의 성적 정렬하기
    score = sorted([list(map(int, input().split())) for _ in range(n)])
    ans = 1
    now_x, now_y = score[0][0], score[0][1]
    for x, y in score[1:] :
        if now_x < x and now_y < y : continue
        now_x, now_y = x, y
        ans += 1
    print(ans)
