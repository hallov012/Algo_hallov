import sys
sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
reverse_data = list(reversed(data))
increase = [1] * n
decrease = [1] * n
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_data[i] > reverse_data[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
ans = 0
for i in range(n):
    temp = increase[i] + decrease[n-i-1] - 1
    ans = max(ans, temp)

print(ans)