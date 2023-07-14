import sys
input = sys.stdin.readline

def check(s, e) :
    for i in range(s, e+1) :
        schedule[i] += 1

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x : [x[0], -x[1]])
schedule = [0] * 366
answer = 0

# 1. start, end 초기 설정
start, end = array[0][0], array[0][1]
check(array[0][0], array[0][1])
# 2. for 문
for s, e in array[1:] :
    # 2-1. 일정이 연속될 경우
    if end + 1 >= s :
        # end 재설정
        if e > end: end = e
    # 2-2. 일정이 연속되지 않을 경우
    else :
        answer += (end - start + 1) * max(schedule[start:end+1])
        start, end = s, e
    check(s, e)
else : answer += (end - start + 1) * max(schedule[start:end+1])
# 결과값에 이어지는 코팅지의 면적 출력
print(answer)