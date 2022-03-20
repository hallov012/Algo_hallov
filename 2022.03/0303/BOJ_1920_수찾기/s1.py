import sys
sys.stdin = open('input.txt')

def binary(num, a_lst, start, end):
    while start <= end:
        middle = (start + end) // 2
        if num == a_lst[middle]:
            return 1
        elif num < a_lst[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return 0

n = int(input())
a_lst = list(map(int, input().split()))
a_lst.sort()
m = int(input())
nums = list(map(int, input().split()))
ans = [0] * m
for num in nums:
    print(binary(num, a_lst, 0, n-1))