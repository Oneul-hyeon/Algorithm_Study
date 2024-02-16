import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    x, y = map(int, input().split())
    # 1. 거리 구하기
    distance = y - x
    # 2. 거리의 제곱근의 정수 부분 구하기
    n = int(distance ** .5)
    # 3. 갯수 업데이트
    ans = 2 * n - 1
    # 4. 나머지 수 생성
    mod = distance - n**2 if n != 1 else distance - 1
    # 5.
    while mod > 0 :
        # 5-1. 나머지 수를 n으로 나눈 몫을 구해 갯수 업데이트
        ans += mod // n
        mod = mod % n
        # 5-2. n 업데이트
        n -= 1
    # 6. 결과 출력
    print(ans)