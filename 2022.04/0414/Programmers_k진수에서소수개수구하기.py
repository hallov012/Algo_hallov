def go_to_hell(n):
    if n == 1:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    # for i in range(100):
    #     if (k ** i) * (k-1) >= n:
    #         m = i
    #         break
    # change = ''
    # for h in range(m, -1, -1):
    #     for i in range(k-1, -1, -1):
    #         if (k ** h) * i <= n:
    #             n -= (k ** h) * i
    #             change += str(i)
    #             break
    change = ''
    while n > 0:
        change = str(n % k) + change
        n //= k

    nums = []
    for num in change.split('0'):
        if num != '':
            nums.append(int(num))

    for a in nums:
        answer += go_to_hell(a)

    return answer

print(solution(1, 6))
print(solution(110011, 10))