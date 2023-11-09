import sys
input = sys.stdin.readline

def solution() :
    while True :
        A, B = map(int, input().split())
        if A == 0 and B == 0 : break
        XA, XB = A, B
        # 1. 리스트 생성
        array_A, array_B = [True, A], [False, B]
        # 2. A 정수 배열 생성
        while XA != 1 :
            XA = XA // 2  if XA % 2 == 0 else 3 * XA + 1
            array_A.append(XA)
        # 3. B 정수 배열 생성
        while XB != 1 :
            XB = XB // 2  if XB % 2 == 0 else 3 * XB + 1
            array_B.append(XB)
        # 4. 최초로 맞는 지점 찾기
        target = 0
        for i in range(-1, -min(len(array_A), len(array_B)) - 1, - 1) :
            if array_A[i] != array_B[i] : target = i; break
        # 5. 결과 출력
        print(f'{A} needs {len(array_A) + target} steps, {B} needs {len(array_B) + target} steps, they meet at {array_A[target+1]}')
if __name__ == "__main__":
    solution()