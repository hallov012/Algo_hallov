import sys
sys.stdin = open('input.txt')

def find(x, y, n):
    check = data[x][y]
    flag = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != check:
                flag = False
                break
    if not flag:
        n //= 3
        for i in range(3):
            for j in range(3):
                find(x+n*i, y+n*j, n)
    else:
        ans_dic[check] += 1

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans_dic = {-1: 0, 0: 0, 1: 0}
find(0, 0, n)
for value in ans_dic.values():
    print(value)