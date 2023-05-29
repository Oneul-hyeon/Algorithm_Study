import sys
input = sys.stdin.readline

def find_p(n, x) :
    if n == 0 :
        if x == 0 : return 0
        else : return 1
    else :
        if x == 1 : return 0
        elif 1 < x <= 1 + len_burger[n-1] : return find_p(n-1, x-1)
        elif x == 2 + len_burger[n-1] : return p[n-1] + 1
        elif 2 + len_burger[n-1] < x <= len_burger[n] - 1 : return p[n-1] + 1 + find_p(n-1, x - 1 - len_burger[n-1] - 1)
        else : return p[n]

n, x = map(int, input().split())
len_burger = [0] * (n+1)
p = [0] * (n+1)

len_burger[0] = 1
p[0] = 1
for i in range(1, n+1) :
    len_burger[i] = 2 * len_burger[i-1] + 3
    p[i] = 2 * p[i-1] + 1

answer = find_p(n, x)
print(answer)