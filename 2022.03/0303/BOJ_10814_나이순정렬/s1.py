import sys
sys.stdin = open('input.txt')

n = int(input())
age_lst = [0] * n
name_lst = [''] * n
idx_lst = list(range(n))
for i in range(n):
    age, name = map(str, input().split())
    age_lst[i] = int(age)
    name_lst[i] = name
for i in range(n-1):
    for j in range(i+1, n):
        if age_lst[i] > age_lst[j]:
            idx_lst[i], idx_lst[j] = idx_lst[j], idx_lst[i]
for idx in idx_lst:
    print(age_lst[idx], name_lst[idx])

