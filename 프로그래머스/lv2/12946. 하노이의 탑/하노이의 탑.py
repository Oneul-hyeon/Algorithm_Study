def solution(n):
    # 1. hanoi 함수 정의
    def hanoi(n) :
        # 1-1. hanoi_sub 함수 실행
        hanoi_sub(n, 1, 3, 2)
    # 2. hanoi_sub 함수 정의
    def hanoi_sub(n, start, end, mid) :
        # 2-1. 종료 조건 설정
        if n == 1 : 
            # 디스크 이동
            move_disk(start, end)
            return
        # 2-2. hanoi_sub 함수 실행
        hanoi_sub(n-1, start, mid, end)
        # 2-3. 디스크 이동
        move_disk(start, end)
        # 2-4. hanoi_sub 함수 실행
        hanoi_sub(n-1, mid, end, start)
    # 3. 디스크 이동 함수 정의
    def move_disk(start, end) :
        # 3-1. 디스크 이동 결과 삽입
        answer.append([start, end])
    answer = []   
    # 4. hanoi 함수 실행
    hanoi(n)
    return answer