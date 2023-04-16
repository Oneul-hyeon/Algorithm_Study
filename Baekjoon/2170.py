import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

n = int(input())

# 1. 두 점의 위치 리스트로 입력받기
array = [list(map(int, input().split())) for _ in range(n)]
# 2. 시작점을 기준으로 입력받기
array.sort()
# 3. 초기 start, end 값 설정 -> 0번 인덱스
start, end = array[0][0], array[0][1]
ans = 0
# 4. for문 -> 1번 인덱스부터 시작
for i in range(1, n) :
    # 4-1. 이미 설정된 start, end 범위 안에 있을 경우 무시
    if array[i][1] <= end : continue
    # 4-2. 선이 이어지는 경우 start는 그대로, end 값 업데이트
    if array[i][0] <= end and array[i][1] > end : end = array[i][1]
    # 4-3. 선이 새로 시작하는 경우 기존의 end - start 값만큼 더해주고 start, end 값 업데이트
    elif array[i][0] > end :
        ans += end - start
        start, end = array[i][0], array[i][1]
ans += end - start

print(ans)




