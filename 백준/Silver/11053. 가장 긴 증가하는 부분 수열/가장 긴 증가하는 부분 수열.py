import sys,bisect
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = []
for i in range(n) :
    if i == 0 :
        dp.append(array[i])
    else :
        if array[i] > dp[-1] :
            dp.append(array[i])
        else :
            idx = bisect.bisect_left(dp, array[i])
            dp[idx] = array[i]
print(len(dp))

