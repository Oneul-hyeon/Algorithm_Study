import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))

# 1. 실수 횟수 리스트 생성
miss = [0] * (n+1)
count = 0
# 2. for문
for i in range(1, n+1) :
    # 각 인덱스에서 실수가 발생할 때마다 총 실수 횟수 + 1
    if array[i] < array[i-1] :
        count += 1
    miss[i] = count

q = int(input())
# 3. 실수 횟수 출력
for _ in range(q) :
    x, y = map(int, input().split())
    print(miss[y] - miss[x])