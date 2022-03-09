import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
temp = list(map(int, input().split()))
ans = sum(temp[:k])
max_ans = ans
for i in range(k, n):
    ans += temp[i]
    ans -= temp[i-k]
    if ans > max_ans:
        max_ans = ans
print(max_ans)