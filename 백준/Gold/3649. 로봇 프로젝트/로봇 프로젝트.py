import sys, math
input = sys.stdin.readline

# 1. 조각 찾기 함수 정의
def find_piece() :
    # 1-1. left, right 설정
    left, right = 0, n-1
    # 1-2.
    while left < right :
        summation = lego[left] + lego[right]
        # 1-2-1. 해당 인덱스 값이 x보다 작은 경우
        if summation < x : left += 1
        # 1-2-2. 해당 인덱스 값이 x보다 큰 경우
        elif summation > x : right -= 1
        # 1-2-3. 해당 인덱스 값의 합이 x와 같은 경우
        else :
            # 결과 출력 후 리턴
            print(f'yes {lego[left]} {lego[right]}')
            return
    # 1-3. 결과 출력 후 리턴
    print('danger')
    return
# 2.
while True :
    try :
        # 2-1. 구멍의 너비 단위 바꾸기
        x = int(input()) * 10 ** 7
        # 2-2. 레고 조각 정렬하기
        n = int(input())
        lego = [0] * n
        for i in range(n) : lego[i] = int(input())
        lego.sort()
        # 2-3. 조각 찾기 함수 실행
        find_piece()
    except : break