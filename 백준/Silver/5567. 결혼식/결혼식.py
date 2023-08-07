import sys

n = int(input())
m = int(input())

friends = [[] for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
ans = set()
for f in friends[1] :
    ans.add(f)
    for fof in friends[f] :
        if fof == 1 : continue
        ans.add(fof)
print(len(ans))