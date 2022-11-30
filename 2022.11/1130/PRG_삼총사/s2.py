def solution(number):
    ans = 0
    n = len(number)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if not number[i] + number[j] + number[k]:
                    ans += 1
    return ans

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))