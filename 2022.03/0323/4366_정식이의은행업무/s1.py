import sys
sys.stdin = open('input.txt')

def to_origin(num_str, x):
    N = len(num_str)
    ans = 0
    for i in range(N):
        ans += int(num_str[0 - i - 1]) * (x ** i)
    return ans

T = int(input())

for tc in range(1, T+1):
    num_bin = input()
    num_tri = input()
    num_bin_lst = []
    num_tri_lst = []
    for i in range(len(num_bin)):
        num = ''
        for j in range(len(num_bin)):
            if i == j:
                if num_bin[i] == '0':
                    num += '1'
                else:
                    num += '0'
            else:
                num += num_bin[j]
        num_bin_lst.append(num)

    for k in range(len(num_tri)):
        num_1, num_2 = '', ''
        for l in range(len(num_tri)):
            if k == l:
                if num_tri[k] == '0':
                    num_1 += '1'
                    num_2 += '2'
                elif num_tri[k] == '1':
                    num_1 += '0'
                    num_2 += '2'
                else:
                    num_1 += '0'
                    num_2 += '1'
            else:
                num_1 += num_tri[l]
                num_2 += num_tri[l]
        num_tri_lst.append(num_1)
        num_tri_lst.append(num_2)

    for a in range(len(num_bin_lst)):
        num = to_origin(num_bin_lst[a], 2)
        num_bin_lst[a] = num

    for b in range(len(num_tri_lst)):
        num = to_origin(num_tri_lst[b], 3)
        num_tri_lst[b] = num

    ans = list(set(num_bin_lst) & set(num_tri_lst))
    print(f'#{tc} {ans[-1]}')