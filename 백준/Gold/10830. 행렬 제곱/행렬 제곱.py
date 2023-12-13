import sys
input = sys.stdin.readline
def solution(n, b, array):
    # 1. 행렬 곱 함수 정의
    def multiple(array1, array2) :
        # 1-1. 출력 리스트 생성
        return_array = []
        # 1-2.
        for row in array1 :
            # 1-2-1. 리스트 생성
            row_array = []
            # 1-2-2.
            for col in zip(*array2) :
                # 원소 값 계산
                value = sum([(x * y) % 1000 for x, y in zip(row, col)]) % 1000
                # 리스트에 값 추가
                row_array.append(value)
            # 1-2-3. 출력 리스트에 값 추가
            return_array.append(row_array)
        # 1-3. 결과 반환
        return return_array
    # 2. 제곱 함수 정의
    def pow(array_pow, b) :
        # 2-1. 종료 조건 설정
        if b == 1 : return array
        # 2-2.
        now_array = pow(array_pow, b // 2)
        # 2-3.
        if b % 2 == 0 : return multiple(now_array, now_array)
        else : return multiple(multiple(now_array, now_array), array)

    for i in range(n) :
        for j in range(n) :
            array[i][j] %= 1000
    # 3.
    answer = pow(array, b)
    for line in answer :
        print(*line)

if __name__ == "__main__" :
    n, b = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    solution(n, b, array)