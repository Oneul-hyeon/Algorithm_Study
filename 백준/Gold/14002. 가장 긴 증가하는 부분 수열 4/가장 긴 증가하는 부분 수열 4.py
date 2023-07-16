import sys, bisect
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [array[0]]
perm = []
for i in range(n):
    if array[i] > dp[-1] :
        dp.append(array[i])
        perm.append((len(dp)-1, array[i]))
    else :
        idx = bisect.bisect_left(dp, array[i])
        dp[idx] = array[i]
        perm.append((idx, array[i]))

ans = []
last_idx = len(dp) -1
for i in range(n-1, -1, -1) :
    if perm[i][0] == last_idx :
        ans.append(perm[i][1])
        last_idx-=1

print(len(dp))
print(*ans[::-1])