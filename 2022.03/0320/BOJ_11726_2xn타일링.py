n = int(input())

ans = [0] * (n+1)
if n in [1, 2]:
    print(n)
    exit()
ans[1] = 1
ans[2] = 2

for i in range(3, n+1):
    ans[i] = ans[i-1] + ans[i-2]

print(ans[n] % 10007)