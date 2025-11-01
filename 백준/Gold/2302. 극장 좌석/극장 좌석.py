import sys
input = sys.stdin.readline

# 1, 수열 리스트 생성
N = int(input())
case = [0 for _ in range(N+1)]
case[0], case[1] = 1, 1
for idx in range(2, N+1):
    case[idx] = sum(case[idx-2:idx])
M = int(input())
# 2. VIP 좌석이 없을 경우
if M == 0 :
    # 2-1. 수열에서 구한 경우의 수 출력
    print(case[N])
# 3. VIP 좌석이 있는 경우
else:
    end, ans = 1, 1
    # 3-1.
    for _ in range(M):
        # 3-1-1. VIP 좌석 번호 입력
        num = int(input())
        # 3-1-2. 연속되는 좌석 수 추출 후 경우의 수 반영
        ans *= (case[seat] if (seat:=num-end) else 1)
        end = num+1
    # 3-2. 마지막 연속되는 좌석의 경우의 수 반영
    ans *= case[N-end+1]
    # 3-3. 총 경우의 수 반환
    print(ans)