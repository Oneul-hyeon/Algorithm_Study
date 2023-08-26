def solution(n):
    # 1. 배열 생성
    array = [[0] * i for i in range(1, n+1)]
    # 2. 입력할 숫자 변수 생성
    num = 1
    # 3. x, y 생성
    x, y = -1, 0
    # 4.
    for direction in range(n) :
        for _ in range(direction, n) :
            # 4-1. 아래로 내려가는 경우
            if direction % 3 == 0 :
                x += 1 # x 값 증가
            # 4-2. 오른쪽으로 이동하는 경우
            elif direction % 3 == 1 :
                y += 1 # y 값 증가
            # 4-3. 위로 올라가는 경우
            else :
                x -= 1; y -= 1 # x, y 값 감소
            # 4-4. 해당 인덱스에 수 입력
            array[x][y] = num
            # 4-5. 숫자 변수 증가
            num += 1
    # 5. 결과 리턴
    return sum(array, [])