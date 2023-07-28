def dfs(m, c) :
    global max_money
    # 종료 조건 설정
    if c == 0 or m == goal :
        if c % 2 != 0 and len(m) == len(set(m)) :
            m[-2], m[-1] = m[-1], m[-2]
        max_money = max(max_money, int(''.join(map(str, m))))
        return
    for i in range(len(m)) :
        for j in range(len(m)) :
            if i < j :
                if m[:i] == goal[:i] :
                    if m[i] != goal[i] and m[j] == goal[i] :
                        m[i], m[j] = m[j], m[i]
                        dfs(m, c - 1)
                        m[i], m[j] = m[j], m[i]

test_case = int(input())
for t in range(1, test_case+1) :
    money, chance = map(int, input().split())
    money = list(map(int, str(money)))
    goal = sorted(money, reverse = True)
    max_money = -int(1e9)
    dfs(money, chance)
    print(f'#{t} {max_money}')