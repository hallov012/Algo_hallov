import sys
sys.stdin = open('input.txt')

n = int(input())
s = input().rstrip()
# 중간 index 2개를 고른 후 그 index를 기준으로 자르면 3개의 문자열이 나옴
s_lst = []
parts = set()
for i in range(1, n-1):
    for j in range(i+1, n):
        a, b, c = s[:i], s[i:j], s[j:]
        parts.add(a)
        parts.add(b)
        parts.add(c)
        s_lst.append((a, b, c))

part_sort = sorted(parts)
ans = 0
for case in s_lst:
    tmp = 0
    for char in case:
        tmp += part_sort.index(char) + 1
    ans = max(ans, tmp)

print(ans)