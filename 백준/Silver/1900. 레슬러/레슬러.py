import sys
input = sys.stdin.readline

n = int(input())
players = [0] + [list(map(int, input().split())) for _ in range(n)]
# 1. 승리 횟수 딕셔너리 생성
win = {}
for i in range(1, n+1) : win[i] = 0
# 2.
for p1 in range(1, n+1) :
    for p2 in range(p1+1, n+1) :
        # 2-1. 승리한 선수의 승리 횟수 추가
        if players[p1][0] + players[p2][0] * players[p1][1] > players[p2][0] + players[p1][0] * players[p2][1] :
            win[p1] += 1
        else : win[p2] += 1
# 3. 이긴 횟수대로 결과 출력
for key, value in sorted(win.items(), key = lambda x : -x[1]) :
    print(key)