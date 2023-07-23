import sys
from math import pi
input = sys.stdin.readline

def check(num) :
    if 0 <= num <= pi :
        return 1
    try :
        num = float_dp[num - 1] + float_dp[num - pi]
    except :
        float_dp[num - 1], float_dp[num - pi] = check(num - 1), check(num - pi)
        num = float_dp[num - 1] + float_dp[num - pi]
    return num

n = int(input())
int_dp = [0] * (n+1) if n > 3 else [0] * 4
int_dp[1], int_dp[2], int_dp[3] = 1, 1, 1

float_dp = dict()
float_dp[4-pi], float_dp[5-pi], float_dp[6-pi] = 1, 1, 1
m = 1000000000000000000
for i in range(4, n+1) :
    int_dp[i] = (int_dp[i-1] + check(i - pi)) % m
print(int_dp[n])