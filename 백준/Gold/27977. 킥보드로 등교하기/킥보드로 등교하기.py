import sys
input = sys.stdin.readline

# 1. left 반환 함수 정의
def return_left(info, l) :
    # 1-1. left 변수 정의
    left = -200_001
    # 1-2.
    for i in range(n) :
        # 1-2-1. 0번 인덱스의 경우
        if i == 0 :
            left = max(info[i], info[i+1] - info[i])
        # 1-2-2. 마지막 인덱스의 경우
        elif i == n - 1 :
            left = max(left, l - info[-1])
        # 1-2-3. 이외의 경우
        else :
            left = max(left, info[i+1] - info[i])
    # 1-3. left 반환
    return left
def solution(l, _, k, info) :
    # 2. left, right 설정
    left, right = return_left(info[:], l), l
    # 3.
    info += [l]
    while left <= right :
        # 3-1. mid 값 설정
        mid = (left + right) // 2
        # 3-2. 주유소 방문 횟수 체크
        cnt, now = 0, mid
        for idx, d in enumerate(info) :
            dist = d - info[idx - 1] if idx > 0 else d
            if now < dist :
                now = mid - dist
                cnt += 1
            else :
                now -= dist
        # 3-3. 방문 횟수가 k보다 큰 경우
        if cnt > k : left = mid + 1
        # 3-4. 방문 횟수가 k보다 작거나 같은 경우
        else : right = mid - 1
    # 4. 결과 출력
    print(left)

if __name__ == "__main__" :
    l, n, k = map(int, input().split())
    info = list(map(int, input().split()))
    solution(l, n, k, info)