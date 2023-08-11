import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def binary_tree(start, end) :
    # 종료 조건 설정
    if start > end : return
    # 오른쪽 서브 트리의 첫 값 찾기
    mid = start + 1
    while mid < len(array) and array[start] > array[mid] :
        mid += 1
    # 왼쪽 서브 트리 구해 시작
    binary_tree(start+1, mid-1)
    # 오른쪽 서브 트리 구해 시작
    binary_tree(mid, end)
    # 루트 노트 출력
    print(array[start])

array = []
while True :
    try :
        # 리스트 입력받기
        array.append(int(input()))
    except :
        break
binary_tree(0, len(array) - 1)