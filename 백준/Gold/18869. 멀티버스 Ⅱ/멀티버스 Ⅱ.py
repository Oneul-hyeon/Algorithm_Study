import sys
input = sys.stdin.readline

# 1. 좌표 압축 함수 정의
def Coordinate_Compression(lst) :
    # 1-1. 중복 제거된 리스트를 정렬
    re_lst = sorted(list(set(lst.copy())))
    # 1-2. 딕셔너리를 사용해 압축된 좌표 부여
    dic = dict()
    for i in range(len(re_lst)) : dic[re_lst[i]] = i+1
    # 1-3. 압축된 좌표 기반 리스트 재생성
    for i in range(n) : lst[i] = dic[lst[i]]
    # 1-4. 결과 리턴
    return lst

m, n = map(int, input().split())
# 2.
multibus = [[] for _ in range(m)]
for i in range(m) : multibus[i] = Coordinate_Compression(list(map(int, input().split()))) # 좌표 압축 함수 실행
# 3.
ans = 0
for i in range(m) :
    for j in range(i+1, m) :
        # 비교 후 카운팅
        if multibus[i] == multibus[j] : ans += 1
# 4. 결과 출력
print(ans)