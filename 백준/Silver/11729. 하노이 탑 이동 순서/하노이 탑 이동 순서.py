import sys
input = sys.stdin.readline

# 1. 메인 재귀함수 생성
def hanoi(n, start, end) :
    # 2. 서브 재귀 함수 호출
    hanoi_sub(n, start, end, 2)

# 3. 서브 재귀함수 생성
def hanoi_sub(n, start, end, other) :
    # 4. 종료 조건 설정
    # 리스트 삽입 함수 실행
    if n == 1 : move_disk(start, end); return

    # 5. 서브 재귀함수 실행 <- part 1
    hanoi_sub(n-1, start, other, end)
    # 6. 리스트 삽입 재귀함수 실행 <- part 2
    move_disk(start, end)
    # 7. 서브 재귀함수 실행 <- part 3
    hanoi_sub(n-1, other, end, start)

# 8. 리스트 삽입 함수 선언
def move_disk(start, end) :
    # 9. 출력 리스트에 이동 현황 삽입
    answer.append((start, end))

n = int(input())
answer = []
# 10. 메인 재귀함수 실행
hanoi(n, 1, 3)


# 11. 결과 출력
print(len(answer))
for direction in answer :
    print(*direction)

