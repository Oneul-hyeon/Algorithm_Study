# -*- coding: utf-8 -*-
import sys
# 해당 지점의 가중치 계산
def get_weight(classroom, student, row, col, n):
    global like_students

    weight = .0
    for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        # classroom 범위 이내인지 확인
        if (check_row := row + r) < 0 or (check_row >= n) or \
                (check_col := col + c) < 0 or (check_col >= n):
            continue
        # 인접한 자리에 학생이 있는 경우, 좋아하는 학생인지 확인
        if (adjoining_seat := classroom[check_row][check_col]) in like_students[student]:
            weight += 1
        # 인접한 자리가 비어있는지 확인
        if not adjoining_seat:
            weight += .1
        weight = round(weight, 1)
    return weight


# 가중치를 이용하여 student가 들어갈 위치 탐색
def get_coord(classroom, student, n):
    MAX_WEIGHT, ROW, COL = 0, 1, 2

    save = {MAX_WEIGHT: -1, ROW: -1, COL: -1}
    for row in range(n):
        for col in range(n):
            # 해당 위치에 학생 배치가 된 경우
            if classroom[row][col]:
                continue
            # 가중치가 저장되어 있는 값보다 적은 경우
            if (weight := get_weight(classroom, student, row, col, n)) <= save[MAX_WEIGHT]:
                continue
            save[MAX_WEIGHT], save[ROW], save[COL] = weight, row, col
    return (save[ROW], save[COL])


like_students = dict()


def solution():
    global like_students

    n = int(sys.stdin.readline())
    classroom = [[0 for _ in range(n)] for _ in range(n)]

    # student dictionary 제작
    for _ in range(n * n):
        student, *likes = map(int, sys.stdin.readline().split())
        like_students[student] = likes

    # classroom에 student 배치
    for student in like_students.keys():
        row, col = get_coord(classroom, student, n)
        classroom[row][col] = student

    points = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

    # 최종 만족도 점수 계산
    point = 0
    for row in range(n):
        for col in range(n):
            weight = get_weight(classroom, classroom[row][col], row, col, n)
            point += points[weight]
    print(point)


if __name__ == "__main__":
    solution()