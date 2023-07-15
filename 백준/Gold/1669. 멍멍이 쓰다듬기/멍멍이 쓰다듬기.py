import sys, math
input = sys.stdin.readline

m, d = map(int, input().split())
diff = d - m
if diff == 0 : print(0)
else :
    diff_sqrt = int(math.sqrt(diff))
    result = 2 * diff_sqrt - 1
    if diff_sqrt**2 == diff : print(result)
    else :
        mod = diff - diff_sqrt ** 2
        print(result + mod // diff_sqrt) if mod % diff_sqrt == 0 else print(result + mod // diff_sqrt + 1)