import sys
input = sys.stdin.readline

def solution(n, array, total) :
    # 1. 조합 함수 정의
    def combination(target, now) :
        state = True
        # 1-1.
        for a, b in array :
            # 필요한 만큼 시약 감소
            now -= (target - b) / a
            if state and (int(now) != now) : state = False
        # 1-2. 시약의 양이 부족하다면 0 출력
        if now < 0 : print(0); exit()
        # 1-3. 정확히 목표 가스 양을 사용했다면 결과 출력 후 종료
        if now == 0 and state : print(target); exit()

    # 2. 최소 시작 값 정의
    target = 1
    # 3.
    while True :
        combination(target, total)
        target += 1

if __name__ == "__main__":
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    total = int(input())
    solution(n, array, total)