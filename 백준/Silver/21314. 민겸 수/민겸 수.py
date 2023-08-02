import sys
input = sys.stdin.readline

string = list(map(str, input().rstrip()))
# 1-1. 최대, 최솟값 변수 생성
max_ = min_ = ''
# 1-2. M 개수 체크 변수 생성
count = 0
# 1-3.
for s in string :
    # 3-1. 해당 문자가 M 인 경우
    if s == 'M' : count += 1
    # 3-2. K 가 나올 경우
    else :
        # M 의 개수가 있는 경우
        if count :
            # 최댓값
            max_ += str((10 ** count) * 5)
            # 최솟값
            min_ += str(10 ** count + 5)
        # M의 개수가 없는 경우
        else :
            max_ += '5'
            min_ += '5'
        # 3-3. M의 개수 초기화
        count = 0
# 4. M 의 개수가 남은 경우
if count :
    # 최댓값
    max_ += '1' * count
    # 최솟값
    min_ += str(10 ** (count - 1))
# 5. 결과 출력
print(f'{max_}\n{min_}')