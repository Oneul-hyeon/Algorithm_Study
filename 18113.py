import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n, k, m = map(int, input().split())
array = [0 for _ in range(n)]
# 1. 김밥을 입력받을 때 K 이하인 것은 제거
# 2. 김밥 꼬다리 처리하기
for i in range(n) :
    kimbab = int(input())
    if kimbab <= k : continue
    elif kimbab < 2*k : kimbab -= k
    else : kimbab -= 2*k
    array[i] = kimbab
# 3. start = 1, end = 손질된 가장 긴 김밥의 길이
start, end =1, max(array)
while start <= end :
    mid = (start+end) // 2
    count = 0
    for i in array :
        count += i//mid
    # 4. 이분탐색을 통해 손질된 김밥의 개수가 m개가 되는 지점 찾기
    if count < m : end = mid - 1
    else : start = mid + 1
# 5. 4를 통해 나오는 지점이 없다면 -1 출력
print(-1) if end == 0 else print(end)



