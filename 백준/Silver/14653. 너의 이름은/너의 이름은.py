import sys
input = sys.stdin.readline

def solution(n, k, q, messages) :
    all = [chr(i) for i in range(66, 65+n)]
    stand = messages[q][0]
    for (not_read, who) in messages[1:] :
        if int(not_read) >= int(stand) :
            try : all.remove(who)
            except : continue
    print(-1) if stand == '0' or not all else print(*all)

if __name__ == '__main__' :
    n, k, q = map(int, input().split())
    messages = [0] + [list(map(str, input().rstrip().split())) for _ in range(k)]
    solution(n, k, q, messages)