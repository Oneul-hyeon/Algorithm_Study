import sys
input = sys.stdin.readline

def check(string) :
    if len(string) == 1 :
        print('YES')
        return
    mid = len(string) // 2
    left, right = string[:mid], string[-mid:][::-1]
    for i in range(mid) :
        if left[i] == right[i]:
            print('NO')
            return
    else :
        check(left)

t = int(input())
for _ in range(t):
    method = list(input().rstrip())
    check(method)