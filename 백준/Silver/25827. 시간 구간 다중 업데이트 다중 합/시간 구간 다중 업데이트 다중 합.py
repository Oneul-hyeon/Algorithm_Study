import sys
input = sys.stdin.readline

def solution(n) :
    # 1. 누적합 수행 함수 정의
    def run_prefix_sum() :
        prefix_sum[0] = change[0]
        # 1-1.
        for i in range(1, l+1) :
            # 점화식에 따라 처리
            prefix_sum[i] = prefix_sum[i-1] + change[i]
        # 1-2.
        for i in range(1, l+1) :
            # 누적합 계산 수행
            prefix_sum[i] += prefix_sum[i-1]

    # 2. 누적합, 변화값 리스트 생성
    l = 24 * 60 * 60
    prefix_sum, change = [0 for _ in range(l+1)], [0 for _ in range(l+1)]
    # 3.누적합 최초 실행 여부 변수 생성
    state = False
    # 4.
    for _ in range(n) :
        information = list(map(str, input().rstrip().split(' ')))
        # 4-1. 시간 구간을 초로 변환
        start, end = sum([x * s for x, s in zip(map(int, information[1].split(':')), [3600, 60, 1]) if x]), sum([x * s for x, s in zip(map(int, information[2].split(':')), [3600, 60, 1]) if x])
        # 4-2. 유형 1의 경우
        if information[0] == '1' :
            # 4-2-1. 변화값 입력
            change[start] += 1
            change[end] -= 1
        # 4-3. 유형 2의 경우
        else :
            # 4-3-1. 최초 누적합 실행
            if not state :
                state = True
                run_prefix_sum()
            # 4-3-2. 값 출력
            print(prefix_sum[end - 1] - prefix_sum[start - 1]) if start else print(prefix_sum[end - 1])
if __name__ == "__main__" :
    n = int(input())
    solution(n)