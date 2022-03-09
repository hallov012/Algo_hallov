for tc in range(1, 11):
    n = int(input())
    data = [input() for _ in range(100)]
    ans = 0
    for i in range(100):
        for a in range(100):
            b = 0
            while a+b < 101:
                word = data[i][a:a+b]
                if word == word[::-1]:
                    len_str = b
                    if len_str > ans:
                        ans = len_str
                b += 1
    for j in range(100):
        col_str = ''
        for i in range(100):
            col_str += data[i][j]
        for a in range(100):
            b = 0
            while a+b < 101:
                word = col_str[a:a+b]
                if word == word[::-1]:
                    len_str = b
                    if len_str > ans:
                        ans = len_str
                b += 1
    print(f'#{tc} {ans}')