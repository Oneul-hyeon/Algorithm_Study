import sys
input = sys.stdin.readline


def solution() :
    # 1. 사람 태우기 함수 정의
    def command_1(i, x) :
        # 1-1. 해당 기차에 x가 없을 경우 삽입
        if x not in array[i] : array[i].append(x)
    # 2. 하차 함수 정의
    def command_2(i, x) :
        # 2-1. 해당 기차에 x가 있을 경우 제거
        try : array[i].pop(array[i].index(x))
        except : return
    # 3. 승객을 뒤로 1칸 미루기 함수 정의
    def command_3(i) :
        out = -1
        # 3-1.
        for x in range(len(array[i])) :
            # 미루기
            array[i][x] += 1
            # 하차해야 하는 경우 승객 체크
            if array[i][x] == 21 : out = x
        # 3-2. 하차해야 하는 경우
        if out != -1 :
            array[i].pop(out)
    # 4. 승객을 앞으로 1칸 당기기 함수 정의
    def command_4(i) :
        out = -1
        # 4-1.
        for x in range(len(array[i])) :
            # 당기기
            array[i][x] -= 1
            # 하차해야 하는 경우 승객 체크
            if array[i][x] == 0 : out = x
        # 4-2. 하차해야 하는 경우
        if out != -1 :
            array[i].pop(out)

    n, m = map(int, input().split())
    # 5. 기차 리스트 생성
    array = [[] for _ in range(n+1)]
    # 6.
    for _ in range(m) :
        # 6-1. 명령 입력받기
        command = list(map(int, input().split()))
        # 6-2. 명령 수행하기
        if command[0] == 1 : command_1(command[1], command[2])
        elif command[0] == 2 : command_2(command[1], command[2])
        elif command[0] == 3 : command_3(command[1])
        elif command[0] == 4 : command_4(command[1])
    # 7. 중복 제거
    ans_lst = []
    for lst in array[1:] :
        if sorted(lst) not in ans_lst : ans_lst.append(sorted(lst))
    # 8. 결과 출력
    print(len(ans_lst))

if __name__ == "__main__":
    solution()