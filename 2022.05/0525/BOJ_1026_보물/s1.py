import sys
sys.stdin = open('input.txt')

n = int(input())
a_list = sorted(list(map(int, input().split())))
b_list = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(n):
    ans += a_list[i] * b_list[i]
print(ans)