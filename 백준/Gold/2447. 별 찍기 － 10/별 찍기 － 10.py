import sys
input = sys.stdin.readline

# 1. 재귀함수 생성
def make_star(n) :
    # 2. 종료 조건 설정
    if n == 1 : return ['*']
    answer = []
    # 3. 재귀함수 실행을 통해 별 생성
    stars = make_star(n//3)
    # 4. for문 -> step의 첫 번째 라인 처리
    for s in stars : answer.append(s * 3)
    # 5. for문 -> step의 두 번째 라인 처리
    for s in stars : answer.append(s + ' ' * (n//3) + s)
    # 6. for문 -> step의 세 번째 라인 처리
    for s in stars : answer.append(s * 3)
    # 7. 리스트 반환
    return answer

n = int(input())
# 8. 재귀함수 실행 & 결과 출력
print("\n".join(make_star(n)))
