import sys
input = sys.stdin.readline

# 1. 수열 함수 정의
def permutation(lst, length, idx) :
    # 1-1. 종료 조건 설정
    if length == m :
        if lst not in ans :
            ans.append(lst)
        return
    # 1-2.
    for i in range(idx, n) :
        # 해당 인덱스 값 리스트에 추가
        permutation(lst + [array[i]], length + 1, i+1)

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

# 2. 출력 리스트 생성
ans = []
# 3. 수열 함수 실행
permutation([], 0, 0)
# 4. 결과출력
for line in ans :
    print(*line)