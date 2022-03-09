def solution(n, arr1, arr2):
    answer = []
    data_1 = ['' * n for _ in range(n)]
    data_2 = ['' * n for _ in range(n)]
    for i in range(n):
        bin_num_1 = bin(arr1[i])[2:]
        line_str_1 = '0' * (n - len(bin_num_1)) + bin_num_1
        bin_num_2 = bin(arr2[i])[2:]
        line_str_2 = '0' * (n - len(bin_num_2)) + bin_num_2
        ans = ''
        for i in range(n):
            if line_str_1[i] == '1' or line_str_2[i] == '1':
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
