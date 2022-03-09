import sys
sys.stdin = open('input.txt')

n = int(input())
card = list(map(int, input().split()))
ans = [1]
for i in range(1, n):
    if not card[i]:
        ans.append(i+1)
    else:
        ans.insert(i-card[i], i+1)
print(*ans)
