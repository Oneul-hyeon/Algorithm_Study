import sys
input = sys.stdin.readline

# 1. 주어진 입력을 ()를 기준으로 나누기
pipes = list(map(str, input().rstrip().split('()')))
ans = 0
now = 0
# 2.
for pipe in pipes :
    for x in pipe :
        # 2-1. 문자열이 '('일 경우와 ')'일 경우 처리
        if x == '(' : now += 1
        elif x == ')' : now -= 1; ans += 1
    # 2-2. 현재 쇠막대기 개수 더해주기
    ans += now
print(ans)