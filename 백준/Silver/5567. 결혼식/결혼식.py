import sys

n = int(input())
m = int(input())

# 1. 친구 여부 리스트 생성
friends = [[] for _ in range(n+1)]
# 2. 친구 정보 입력
for _ in range(m) :
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
ans = set()
# 3.
for f in friends[1] :
    # 3-1. 상근이의 친구 카운트
    ans.add(f)
    # 3-2.
    for fof in friends[f] :
        # 상근이 친구의 친구 카운트
        if fof == 1 : continue
        ans.add(fof)
# 4. 결과 출력
print(len(ans))