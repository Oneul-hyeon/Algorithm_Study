import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
# 1. 리스트 생성
# 2. 초기값 설정
time, text = [0], ['']
# 3.
for _ in range(n) :
    # 3-1. 명령과 수행시간 입력받기
    command, info, t = map(str, input().rstrip().split())
    # 3-2. 수행 시간 삽입
    time.append(int(t))
    # 3-3. 'type' 명령일 경우
    if command == 'type' :
        # 이전 텍스트에서 문자 추가
        text.append(text[-1] + info)
    # 3-4. 'undo' 명령일 경우
    else :
        # 이전 t 초의 인덱스 구하기
        index = bisect_left(time, int(t) - int(info)) - 1
        # 해당 인덱스의 텍스트 값 삽입
        text.append(text[index if index >= 0 else 0])
# 4. 결과 출력
print(text[-1])