import sys
input = sys.stdin.readline
state = False
def solution(n) :
    # 1. 명령 1
    def command(c,start, end) :
        global state
        # 1-1. 시, 분, 초 정보를 초 정보로 변환
        start = sum([x*y for x, y in zip(map(int, start.split(":")), [3600, 60, 1]) if x])
        end = sum([x*y for x, y in  zip(map(int, end.split(":")), [3600, 60, 1])if x])
        # 1-2. 명령 1일 경우
        if c == '1' :
            # 누적합을 위한 값 삽입
            for i in range(start+1, end+1) :
                seconds[i] += 1
        # 1-3. 명령 2일 경우
        else :
            # 1-3-1. 최초 누적합 수행
            if not state : prefix_sum()
            # 1-3-2. 값 출력
            print(seconds[end] - seconds[start])
    # 2. 누적합
    def prefix_sum() :
        global state
        state = True
        for i in range(2, 24 * 60 * 60 + 1) :
            seconds[i] += seconds[i-1]
    # 3. 초 당 배열 생성
    seconds = [0 for _ in range(24*60*60 + 1)]
    # 4.
    for _ in range(n) :
        c, start, end = map(str, input().rstrip().split(' '))
        command(c, start, end)

if __name__ == "__main__" :
    n = int(input())
    solution(n)