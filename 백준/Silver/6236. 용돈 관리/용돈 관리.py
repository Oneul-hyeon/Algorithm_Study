import sys
input = sys.stdin.readline

def solution() :
    n, m = map(int, input().split())
    array = [int(input()) for _ in range(n)]
    # 1. left, right 설정
    left, right = max(array), sum(array)
    # 2.
    while left <= right :
        # 2-1. mid 값 설정
        mid = (left + right) // 2
        # 2-2. 인출 횟수 카운트
        cnt = 0
        now = 0
        for money in array :
            # 2-2-1. 돈이 부족할 경우
            if now < money :
                now = mid - money
                cnt += 1
            # 2-2-2. 돈이 부족하지 않을 경우
            else :
                now -= money
        # 2-3. 최소금액을 구하는 것이므로
        if cnt <= m :
            right = mid - 1
        else :
            left = mid + 1
    # 3. 결과 출력
    print(left)
if __name__ == "__main__":
    solution()