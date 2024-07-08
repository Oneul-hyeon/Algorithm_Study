import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 1. 스택 생성
stack = []
# 2.
for idx, height in enumerate(array) :
    # 2-1.
    while stack and stack[-1][0] < height :
        # 스택에서 값 제거
        stack.pop()
    # 2-2. 스택에 값이 없을 경우 0 출력
    # 2-3. 스택에 값이 있을 경우 스택 마지막 값의 인덱스 출력
    print(stack[-1][1] if stack else 0, end = " ")
    # 2-4. 스택에 (현재 높이, 현재 인덱스 삽입)
    stack.append((height, idx+1))