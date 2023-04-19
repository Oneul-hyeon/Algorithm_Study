import sys
input = sys.stdin.readline

# 1. 재귀함수 선언
def backtracking(array, energy) :
    global max_energy
    # 2. 종료 조건 설정
    # 리스트의 길이가 2일 때
    if len(array) == 2 :
        # 최댓값 비교 후 초기화
        if max_energy < energy : max_energy = energy
        return
    # 3. for문 -> 범위는 1부터 리스트의 길이 -1 까지
    for i in range(1, len(array) - 1) :
        # 3-1. 재귀함수 실행
        # 인자 : 해당 i를 제거한 리스트, 계산된 에너지
        backtracking(array[:i] + array[i+1:], energy + array[i-1] * array[i+1])

max_energy = -int(1e9)
n = int(input())
# 4. 구슬 입력받기
lst = list(map(int, input().split()))
# 5. 재귀함수 실행
backtracking(lst, 0)
print(max_energy)