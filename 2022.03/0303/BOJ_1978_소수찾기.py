n = int(input())
nums = list(map(int, input().split()))
ans = 0
for num in nums:
    error = 0
    if num > 1:
        for i in range(2, num):
            if not num % i:
                error += 1
        if not error:
            ans += 1
print(ans)