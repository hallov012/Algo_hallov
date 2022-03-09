import sys
sys.stdin = open('input.txt')

data = [int(input()) for _ in range(9)]
for i in range(1<<9):
    subset = []
    for j in range(9):
        if i & (1<<j):
            subset.append(data[j])
    if len(subset) == 7 and sum(subset) == 100:
        subset.sort()
        print(*subset, sep='\n')
        break


