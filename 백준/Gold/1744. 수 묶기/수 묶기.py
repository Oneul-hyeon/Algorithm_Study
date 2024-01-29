import sys
input = sys.stdin.readline

n = int(input())

# 1. 양수 리스트, 음수 리스트 생성
positive, negative = [], []
# 2. 수 입력받기
zero = 1
for _ in range(n) :
    num = int(input())
    if num > 0 : positive.append(num)
    elif num < 0 : negative.append(num)
    else :
        if zero == 1 : zero = 0
# 3. 리스트 정렬
positive.sort(reverse = True)
negative.sort()
# 4. 변수 생성
ans = 0
# 5. 양수 리스트 길이가 홀수일 경우 마지막 값 더하기
if len(positive) % 2 != 0 : ans += positive[-1]
# 6. 음수 리스트 길이가 홀수일 경우 마지막 값 더하기
if len(negative) % 2 != 0 : ans += negative[-1] * zero
# 7. 연속된 양수를 곱해 더하기
for i in range(0, len(positive), 2) :
    if i+1 < len(positive) :
        ans += positive[i] + positive[i+1] if positive[i] == 1 or positive[i+1] == 1 else positive[i] * positive[i+1]
# 8. 연속된 음수를 곱해 더하기
for i in range(0, len(negative), 2) :
    if i + 1 < len(negative) :
        ans += negative[i] * negative[i+1]
# 9. 결과 출력
print(ans)