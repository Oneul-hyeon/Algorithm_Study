import sys
input = sys.stdin.readline
n = int(input())
array = [input().rstrip().split() for _ in range(n)]
count_0, count_1 = 0, 0
def quadtree(x, y, size) :
    global count_0, count_1

    first_node = array[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if array[i][j] != first_node:
                break
        else :
            continue
        break
    else :
        if first_node == '0':
            count_0+=1
        else:
            count_1+=1
        return
    # 색이 다른 경우
    size //= 2
    quadtree(x, y, size)
    quadtree(x, y+size, size)
    quadtree(x+size, y, size)
    quadtree(x+size, y+size, size)

quadtree(0, 0, n)
print(count_0)
print(count_1)