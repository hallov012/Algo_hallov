import sys
sys.stdin = open('input.txt')

def find(x, y, n):
    global ans
    check = data[x][y]
    flag = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != check:
                flag = False
                break
    if not flag:
        ans += '('
        n //= 2
        find(x, y, n)
        find(x, y+n, n)
        find(x+n, y, n)
        find(x+n, y+n, n)
        ans += ')'
    else:
        ans += str(check)

input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().strip())) for _ in range(n)]
ans = ''
find(0, 0, n)
print(ans)
