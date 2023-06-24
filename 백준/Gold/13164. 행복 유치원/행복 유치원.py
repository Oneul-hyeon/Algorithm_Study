import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = sorted(list(map(int, input().split())))
ans = [0] * (len(array) - 1)

for i in range(n-1) : ans[i] = array[i+1] - array[i]

ans.sort(reverse = True)
print(sum(ans[k-1:]))