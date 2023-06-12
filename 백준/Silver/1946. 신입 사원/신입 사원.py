import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    # 1. 순위 정렬
    score = sorted([list(map(int, input().split())) for _ in range(n)])
    # 2. 비교 인덱스 순위 설정
    now = score[0]
    ans = 1
    # 3.
    for i in range(1, n) :
        # 4. 비교 인덱스보다 순위가 낮을 경우 뽑힐 수 없으므로 continue
        if now[1] < score[i][1] : continue
        # 5. 이외의 경우 뽑히므로 카운트 후 비교 인덱스 갱신
        ans += 1
        now = score[i]
    # 6. 결과 출력
    print(ans)