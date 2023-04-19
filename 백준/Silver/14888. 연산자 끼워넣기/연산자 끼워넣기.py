import sys, math

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
plus, sub, mul, div = map(int, sys.stdin.readline().split())

def dfs(id, sum, plus, sub, mul, div):
    global min_, max_
    if id == n :
        min_ = min(min_, sum)
        max_ = max(max_, sum)
        return
    if plus :
        dfs(id+1, sum+numbers[id], plus-1, sub, mul, div)
    if sub :
        dfs(id+1,sum-numbers[id],plus, sub-1, mul, div)
    if mul :
        dfs(id+1,sum*numbers[id],plus, sub, mul-1, div)
    if div :
        if sum < 0 : dfs(id+1,-(-sum//numbers[id]), plus, sub, mul, div-1)
        else : dfs(id+1,sum//numbers[id], plus, sub, mul, div-1)

min_, max_ = math.inf, -math.inf
id = 1
dfs(id, numbers[0], plus, sub, mul, div)
print(max_)
print(min_)