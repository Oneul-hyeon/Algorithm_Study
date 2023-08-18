import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
start_member = []

def dfs():
    global min_
    if len(start_member) == int(n/2) :
        start = 0
        rink = 0
        rink_member = [x for x in range(n) if x not in start_member]
        for i in range(len(start_member)) :
            for j in range(i+1, len(start_member)) :
                if i!=j :
                    start += array[start_member[i]][start_member[j]] + array[start_member[j]][start_member[i]]
        for i in range(len(rink_member)) :
            for j in range(i+1, len(rink_member)) :
                if i!=j :
                    rink += array[rink_member[i]][rink_member[j]] + array[rink_member[j]][rink_member[i]]
        if abs(rink - start) < min_ :
            min_ = abs(rink - start)
        return

    for i in range(n) :
        if start_member == []:
            start_member.append(i)
            dfs()
            start_member.pop()
        else :
            if start_member[-1] < i :
                start_member.append(i)
                dfs()
                start_member.pop()
min_ = int(1e9)
dfs()
print(min_)