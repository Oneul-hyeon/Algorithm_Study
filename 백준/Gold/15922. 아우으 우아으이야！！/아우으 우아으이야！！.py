import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
# 1. start, end 설정
p_start, p_end = array[0][0], array[0][1]
# 2. 출력 변수 설정
answer = p_end - p_start
# 3.
for i in range(1, n) :
    start, end = array[i][0], array[i][1]
    # 3-1. 이전의 end 값이 현재 end 값보다 클 경우
    if p_end >= end : continue
    # 3-2. 이전의 end 값이 현재 start 값보다 클 경우
    elif p_end > start : start = p_end
    # 3-3. 결과 더하기
    answer += end - start
    # 3-4. 이전의 start, end 값 재정의
    if p_end < end :
        p_start, p_end = start, end
# 4. 결과 출력
print(answer)