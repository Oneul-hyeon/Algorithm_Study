import sys
input = sys.stdin.readline

ans = -int(1e9)
def solution(n, m, array, RANGE, MERRY) :
    # 1. 백트래킹 함수 정의
    def backtracking(who, i, summation) :
        global ans
        # 1-1. 종료 조건 설정
        if i == m :
            # 1-1-1. 랑이인 경우
            if who == 'R' :
                # 메리 만족도 체크를 위한 백트래킹 실행
                backtracking('M', 0, summation)
            # 1-1-2. 메리인 경우
            else :
                # 최댓값 업데이트
                ans = max(ans, summation)
            return
        # 1-2.
        for j in range(n) :
            # 1-2-1. 캔이 없을 경우 continue
            if array[j] == 0 : continue
            # 1-2-2. 캔 개수 차감
            array[j] -= 1
            # 1-2-3. 백트래킹 실행
            if who == 'R' : backtracking(who, i+1, summation + RANGE[i][j])
            else : backtracking(who, i+1, summation + MERRY[i][j])
            # 1-2-4. 캔 개수 증가
            array[j] += 1
    # 2. 랑이 만족도 체크를 위한 백트래킹 실행
    backtracking('R', 0, 0)
    # 3. 결과 출력
    print(ans)

if __name__ == "__main__":
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    RANGE = [list(map(int, input().split())) for _ in range(m)]
    MERRY = [list(map(int, input().split())) for _ in range(m)]
    solution(n, m, array, RANGE, MERRY)