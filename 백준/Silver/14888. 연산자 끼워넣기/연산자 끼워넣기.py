import sys
input = sys.stdin.readline

# 1. 백트래킹 함수 정의
def backtracking(num, idx, plus, sub, mul, div) :
    global max_ans, min_ans
    # 1-1. 종료조건 설정
    if idx == n :
        # 최댓값 업데이트
        max_ans = max(max_ans, num)
        # 최솟값 업데이트
        min_ans = min(min_ans, num)
        return
    # 1-2. 더하기 개수가 남은 경우
    if plus : backtracking(num + numbers[idx], idx + 1, plus - 1, sub, mul, div)
    # 1-3. 빼기 개수가 남은 경우
    if sub : backtracking(num - numbers[idx], idx + 1, plus, sub - 1, mul, div)
    # 1-4. 곱하기 개수가 남은 경우
    if mul : backtracking(num * numbers[idx], idx + 1, plus, sub, mul - 1, div)
    # 1-5. 나누기 개수가 남은 경우
    if div : backtracking(num // numbers[idx], idx + 1, plus, sub, mul, div - 1) if num > 0 else backtracking(-(abs(num) // numbers[idx]), idx + 1, plus, sub, mul, div - 1)

n = int(input())
numbers = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())
max_ans, min_ans = -sys.maxsize, sys.maxsize
# 2. 백트래킹 함수 실행
backtracking(numbers[0], 1, plus, sub, mul, div)
# 3. 결과 출력
print(f'{max_ans}\n{min_ans}')