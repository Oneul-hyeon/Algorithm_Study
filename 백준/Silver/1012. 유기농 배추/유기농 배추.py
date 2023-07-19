import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y) :
    if x < 0 or x >= n or y < 0 or y >= m :
        return False

    if array[x][y] == 1:
        array[x][y] = 0
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False

test_case = int(input())

for _ in range(test_case) :
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1
    count = 0
    for i in range(n) :
        for j in range(m) :
            if dfs(i, j) :
                count += 1
    print(count)



