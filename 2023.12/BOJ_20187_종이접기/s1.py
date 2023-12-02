import sys
sys.stdin = open('input.txt')

k = int(input())
orders = list(map(str, input().split()))
h = int(input())
# D => 위에서 아래로 1 => 3, 0 => 2
# U => 아래서 위로 3 => 1, 2 => 0
# R => 왼쪽에서 오른쪽으로 0 => 1, 2 => 3
# L => 오른쪽에서 왼쪽으로 1 => 0, 3 => 2

counter = {
    'D': 'U',
    'U': 'D',
    'R': 'L',
    'L': 'R'
}

find = {
    'D':  {
        1: 3,
        0: 2,
    },
    'U': {
        3: 1,
        2: 0,
    },
    'R': {
        0: 1,
        2: 3,
    },
    'L': {
        1: 0,
        3: 2,
    }
}

arr = [[h]]
r, c = 1, 1
orders.reverse()
for order in orders:
    order = counter[order]
    if order in ('UD'):
        new_arr = [[-1] * (r*2) for _ in range(c)]
        if order == 'U':
            for i in range(r):
                for j in range(c):
                    new_arr[r+i-1][j] = arr[i][j]
                    new_arr[r-i-1][j] = find[order][arr[i][j]]
        else:
            for i in range(r):
                for j in range(c):
                    new_arr[i][j] = arr[i][j]
                    new_arr[2*r-i-1][j] = find[order][arr[i][j]]
        r *= 2
    else:
        new_arr = [[-1] * r for _ in range(c*2)]
        if order == 'R':
            for i in range(r):
                for j in range(c):
                    new_arr[i][j] = arr[i][j]
                    new_arr[i][2*c-j-1] = find[order][arr[i][j]]
        else:
            for i in range(r):
                for j in range(c):
                    new_arr[i][c+j-1] = arr[i][j]
                    new_arr[i][c-j-1] = find[order][arr[i][j]]
        c *= 2
    arr = new_arr










