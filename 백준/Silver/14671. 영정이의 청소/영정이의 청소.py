import sys
input = sys.stdin.readline

def solution() :
    _, _, k = map(int, input().split())
    # 1. 리스트 생성
    array = [False for _ in range(4)]
    # 2.
    for _ in range(k) :
        x, y = map(int, input().split())
        if x % 2 != 0 and y % 2 != 0 and not array[0] : array[0] = True
        elif x % 2 != 0 and y % 2 == 0 and not array[1] : array[1] = True
        elif x % 2 == 0 and y % 2 != 0 and not array[2]: array[2] = True
        elif x % 2 == 0 and y % 2 == 0 and not array[3]: array[3] = True
    # 3. 결과 출력
    print("YES") if array.count(True) == 4 else print("NO")

if __name__ == "__main__":
    solution()