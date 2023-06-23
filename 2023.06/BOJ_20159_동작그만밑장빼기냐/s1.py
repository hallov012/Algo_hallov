import sys
sys.stdin = open('input.txt')

n = int(input())
cards = [0] + list(map(int, input().split()))
odd_sum = [0] 
even_sum = [0]
for i in range(1, n+1):
    if i % 2:
        odd_sum.append(cards[i] + odd_sum[-1])
        even_sum.append(even_sum[-1])
    else:
        odd_sum.append(odd_sum[-1])
        even_sum.append(cards[i] + even_sum[-1])
ans = odd_sum[-1]

print(odd_sum)
print(even_sum)
for i in range(1, n+1):
    if i % 2:
        temp = odd_sum[i-1] + (even_sum[-1] - even_sum[i])
    else:
        temp = odd_sum[i] + (even_sum[-2] - even_sum[i-1])
    ans = max(ans, temp)
print(ans)
