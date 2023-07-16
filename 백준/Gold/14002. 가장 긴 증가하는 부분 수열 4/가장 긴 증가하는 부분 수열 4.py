import sys, bisect
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1. 결과값 출력에 사용할 리스트 생성
result = [array[0]]
# 2. 갱신되는 인덱스의 위치와 값 설정을 위한 리스트 생성
perm = [(0, array[0])]
# 3. 리스트의 가장 큰 수와 비교
for i in range(1, n):
    # 3-1. 입력받은 수가 리스트의 가장 큰 수보다 클 경우
    if array[i] > result[-1] :
        result.append(array[i])
        # 인덱스의 위치와 값 저장
        perm.append((len(result)-1, array[i]))
    # 3-2. 입력받은 수가 리스트의 가장 큰 수보다 작을 경우
    else :
        # 값 초기화
        idx = bisect.bisect_left(result, array[i])
        result[idx] = array[i]
        # 인덱스의 위치와 값 저장
        perm.append((idx, array[i]))

ans = []
# 4. 생성된 리스트의 길이 정의
last_idx = len(result) - 1
for i in range(n-1, -1, -1) :
    # 4-1. 인덱스 순서에 맞게 출력 리스트에 삽입
    if perm[i][0] == last_idx :
        ans.append(perm[i][1])
        last_idx-=1

# 결과 출력
print(len(result))
print(*ans[::-1])