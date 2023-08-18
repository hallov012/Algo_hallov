import sys
sys.stdin = open('input.txt')

n = int(input())
k_lst = list(map(int, input().split()))
max_num = max(k_lst)
idx = k_lst.index(max_num)

for i in range(1, idx+1):
    if k_lst[i] < k_lst[i-1]:
        print(0)
        exit()

for j in range(idx+1, n):
    if k_lst[j] > k_lst[j-1]:
        print(0)
        exit()

print(sum(k_lst))



