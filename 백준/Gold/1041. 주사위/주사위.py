import sys
input = sys.stdin.readline

# 1. 2면이 보이는 주사위의 최솟값 함수 정의
def return_section2() :
    # 1-1. 변수 생성
    value = int(1e9)
    # 1-2.
    for x in range(6) :
        for y in range(x+1, 6) :
            # 제외되는 경우는 continue
            if (x, y) in except_case2 : continue
            # 최솟값 업데이트
            value = min(value, dice[x] + dice[y])
    # 1-3. 결과 리턴
    return value
# 2. 3면이 보이는 주사위의 최솟값 함수 정의
def return_section3() :
    # 2-1. 변수 생성
    value = int(1e9)
    # 2-2.
    for x, y, z in case3 :
        # 최솟값 업데이트
        value = min(value, dice[x] + dice[y] + dice[z])
    # 2-3. 결과 리턴
    return value

n = int(input())
dice = list(map(int, input().split()))

except_case2 = [(0, 5), (2, 3), (1, 4)]
case3 = [(0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 4), (1, 2, 5), (2, 4, 5), (1, 3, 5), (3, 4, 5)]

# 3. n = 1일 경우
if n == 1 : print(sum(dice) - max(dice))
# 4. 이외의 경우
else :
    # 4-1. 1면이 보이는 주사위의 최솟값 생성
    section1 = min(dice)
    # 4-2. 2면이 보이는 주사위의 최솟값 생성
    section2 = return_section2()
    # 4-3. 3면이 보이는 주사위의 최솟값 생성
    section3 = return_section3()
    # 4-4. 결과 출력
    print(section3 * 4 + section2 * ((n-1) * 4 + (n-2) * 4) + section1 * ((n-2) * (n-2) + (n-1) * (n-2) * 4))