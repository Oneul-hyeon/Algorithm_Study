import sys
sys.stdin = open('input.txt','r')

input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key = lambda x : [x[1], x[0]])
end = array[0][1]
count = 1
for line in array :
    if end <= line[0] :
        count += 1
        end = line[1]
print(count)