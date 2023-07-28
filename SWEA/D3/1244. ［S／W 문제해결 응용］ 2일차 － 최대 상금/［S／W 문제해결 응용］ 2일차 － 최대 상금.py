# 1. dfs 함수 실행
def dfs(m, c) :
    global max_money
    # 1-1. 종료 조건 설정 <- 교환 횟수를 소진하거나 소진 전에 최대 상금에 도달할 경우
    if c == 0 or m == goal :
        # 남은 교환 횟수가 홀수이면서 중복되는 수가 없는 경우
        if c % 2 != 0 and len(m) == len(set(m)) :
            m[-2], m[-1] = m[-1], m[-2]
        # 최댓값 갱신
        max_money = max(max_money, int(''.join(map(str, m))))
        return
    # 1-2.
    for i in range(len(m)) :
        if m[:i] == goal[:i] :
            for j in range(len(m)) :
                    if m[i] != goal[i] and m[j] == goal[i] :
                        m[i], m[j] = m[j], m[i]
                        dfs(m, c - 1)
                        m[i], m[j] = m[j], m[i]

test_case = int(input())
for t in range(1, test_case+1) :
    money, chance = map(int, input().split())
    # 2. 숫자판 리스트화시키기
    money = list(map(int, str(money)))
    # 3. 최대 상금 설정
    goal = sorted(money, reverse = True)
    max_money = -int(1e9)
    # 4. dfs 실행
    dfs(money, chance)
    # 5. 결과 출력
    print(f'#{t} {max_money}')