def solution(number):
    ans = 0
    n = len(number)
    number.sort()
    for i in range(n-2):
        target = -number[i]
        left, right = i+1, n-1
        while left < right:
            temp = number[left] + number[right]
            if temp == target:
                left += 1
                if number[i] == number[left] ==number[right] == 0:
                    ans += number.count(0)
                ans += number.count(number[right])
            elif temp < target:
                left += 1
            else:
                right -= 1
    return ans

# print(solution([-2, 3, 0, 2, -5]))
print(solution([-1, -1, -1, 2, 2]))
# print(solution([-1, 1, -1, 1]))