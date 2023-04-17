import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = []
def backtracking() :
    if len(line) == m :
        print(*line)
        return
    for i in range(1, n+1) :
        line.append(i)
        backtracking()
        line.pop()
backtracking()