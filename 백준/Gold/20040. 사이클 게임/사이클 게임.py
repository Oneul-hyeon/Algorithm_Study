import sys
input = sys.stdin.readline

# 1. Union 함수 생성
def Union(a, b):
    # 1-1. 두 노드의 루트 노트 탐색
    a = Find(a)
    b = Find(b)
    # 1-2. 크기가 더 작은 노드에 결과 저장
    if a > b:
        root[a] = b
    else:
        root[b] = a

# 2. Find 함수 생성
def Find(x):
    # 2-1. 해당 노드가 루트 노드가 아닌 경우
    if x!=root[x]:
        return Find(root[x])
    # 2-2. 루트 노드 반환
    return x

n, m = map(int, input().split())

# 3. 루트 노드 리스트 생성
root = [idx for idx in range(n)]
# 4.
for idx in range(1, m+1):
    a, b = map(int, input().split())
    # 4-1. 두 노드의 사이클이 연결되어 있는 경우 해당 순서 출력 후 break
    if Find(a)==Find(b):
        print(idx)
        break
    # 4-2. 연결되어 있지 않은 경우 두 노드 연결
    else:
        Union(a, b)
# 5. 게임이 종료되지 않은 경우 0 출력
else:
    print(0)