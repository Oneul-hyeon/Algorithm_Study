import sys, math
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int,input().split()))
distance = [abs(node - s) for node in array]
for i in distance :
    try :
        gcd_ = math.gcd(gcd_, i)
    except :
        gcd_ = i
print(gcd_)