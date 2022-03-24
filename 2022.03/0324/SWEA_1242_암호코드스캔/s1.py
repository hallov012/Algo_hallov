import sys
sys.stdin = open('input.txt')

T = int(input())

bi_sol = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
          '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
          'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
code_sol = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
            (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9}

for tc in range(1, T+1):
    n, m = map(int, input().split())
    data = set()
    for _ in range(n):
        data.add(input().strip())
    data = sorted(list(data))
    data.pop(0)

    codes = []
    code_origin = []
    ans = 0
    for i in range(len(data)):
        binary = ''
        for char in data[i]:
            binary += bi_sol[char]
        a, b, c, d = 0, 0, 0, 0
        rate_lst = []
        for j in range(len(binary)-1, -1, -1):
            if binary[j] == '1' and c == 0:
                d += 1
            elif binary[j] == '0' and d != 0 and b == 0:
                c += 1
            elif binary[j] == '1' and a == 0:
                b += 1
            elif binary[j] == '0' and b != 0:
                a += 1
                if binary[j-1] == '1' or j == 0:
                    min_num = min(a, b, c, d)
                    rate_lst.append((b//min_num, c//min_num, d//min_num))
                    a, b, c, d = 0, 0, 0, 0
                    if len(rate_lst) == 8:
                        if rate_lst not in codes:
                            codes.append(rate_lst)
                        rate_lst = []
    for code in codes:
        num_lst = []
        for k in range(7, -1, -1):
            num_lst.append(code_sol[code[k]])
        code_origin.append(num_lst)

    for num_code in code_origin:
        check = 0
        for i in range(8):
            if i % 2:
                check += num_code[i]
            else:
                check += 3 * num_code[i]
        if not check % 10:
            ans += sum(num_code)

    print(f'#{tc} {ans}')
