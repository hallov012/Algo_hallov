import sys
sys.stdin = open('input.txt')

T = int(input())

code_sol = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = [input() for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(m-1, -1, -1):
            if data[i][j] == '1':
                ex = i
                ey = j
                break
    code = data[ex][ey-55:ey+1]
    for a in range(8):
        num_code = code[7 * a: 7 * (a+1)]
        ans.append(code_sol[num_code])

    check = 0
    for i in range(8):
        if i % 2:
            check += ans[i]
        else:
            check += 3 * ans[i]

    if not check % 10:
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} 0')
