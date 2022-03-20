import sys
sys.stdin = open('input.txt')

def pater_cut(n, row, col): # row, col 색종이의 제일 왼쪽 위 idx
    global ans
    if n == 1:
        if paper[row][col] == 0:
            ans[0] += 1
        else:
            ans[1] += 1
        return

    middle = n // 2
    paper_sum_1 = sum(sum(paper[y][col:col+middle]) for y in range(row, row+middle))
    paper_sum_2 = sum(sum(paper[y][col+middle:col+middle*2]) for y in range(row, row+middle))
    paper_sum_3 = sum(sum(paper[y][col:col+middle]) for y in range(row+middle, row+middle*2))
    paper_sum_4 = sum(sum(paper[y][col+middle:col+middle*2]) for y in range(row+middle, row+middle*2))

    if paper_sum_1 == 0:
        ans[0] += 1
    elif paper_sum_1 == middle ** 2:
        ans[1] += 1
    else:
        pater_cut(n//2, row, col)

    if paper_sum_2 == 0:
        ans[0] += 1
    elif paper_sum_2 == middle ** 2:
        ans[1] += 1
    else:
        pater_cut(n // 2, row, col+middle)

    if paper_sum_3 == 0:
        ans[0] += 1
    elif paper_sum_3 == middle ** 2:
        ans[1] += 1
    else:
        pater_cut(n // 2, row+middle, col)

    if paper_sum_4 == 0:
        ans[0] += 1
    elif paper_sum_4 == middle ** 2:
        ans[1] += 1
    else:
        pater_cut(n // 2, row+middle, col+middle)

    return



n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0] # 흰색, 파랑색
biggest = sum([sum(line) for line in paper])
if biggest == 0:
    print(1)
    print(0)
    exit()
elif biggest == n ** 2:
    print(0)
    print(1)
    exit()
pater_cut(n, 0, 0)
print(ans[0])
print(ans[1])


