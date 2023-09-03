import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trust = list(map(int, input().split()))
# 1. 진실을 아는 사람이 없을 경우
if not trust[0] : print(m)
# 2. 진실을 아는 사람이 있을 경우
else :
    # 2-1. 진실을 알고 있는 사람 리스트 생성
    trust = set(trust[1:])
    # 2-2.
    information = []
    for _ in range(m) :
        # 리스트에 파티 정보 담기
        information.append(list(map(int, input().split())))
    # 2-3. 
    for info in information * m :
        # 진실을 알 수 있는 사람이 포함되어 있는지 여부 체크
        if len(trust & set(info[1:])) > 0 :
            # 포함되어 있을 경우 진실 여부 업데이트
            trust = trust.union(set(info[1:]))
    # 2-4. 과장된 이야기를 할 수 있는 파티 개수 체크
    cnt = 0
    for info in information :
        # 진실을 알 수 있는 사람이 포함되어 있는지 여부 체크
        if len(trust & set(info[1:])) == 0 : cnt += 1
    # 2-5. 결과 출력
    print(cnt)