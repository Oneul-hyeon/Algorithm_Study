N = int(input())
if N % 2 == 1:  # odd
    ans = N * (N - 1) // 2
else:           # even
    ans = (N * N - 2) // 2

print(ans)