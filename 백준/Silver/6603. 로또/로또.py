import sys
input = sys.stdin.readline

# 2. 재귀 함수 만들기
def backtracking():
    # 2-1. 종료 조건 설정
    if len(array) == 6:
        print(*array)
        return
    # 2-2. for문
    for i in range(1, len(rotto_number)):
        # 2-2-1. 리스트에 정렬된 로또 번호의 i 번째 인덱스 값 append
        # 로또 번호가 겹치면 안 됨
        if rotto_number[i] not in array:
            # 리스트가 비었거나 리스트에 담긴 로또 번호의 마지막 값이 rotto_number[i]보다 작을 때(정렬된 상태로 출력해야 하므로)
            if not array or rotto_number[i] > array[-1]:
                array.append(rotto_number[i])
                # 2-2-2. 재귀 함수 실행
                backtracking()
                # 2-2-3. 리스트의 마지막 값 빼기
                array.pop()

while True :
    rotto_number = list(map(int, input().split()))
    if rotto_number == [0] : break
    else :
        # 1. 백트래킹에 사용될 리스트 만들기
        array = []
        backtracking()
        print('')