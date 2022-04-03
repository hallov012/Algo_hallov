def solution(number, k):
    answer = ''
    nums = list(map(int, number))
    n = len(nums)
    i = 0
    m = n - k
    while m > 0:
        max_num = -1
        max_idx = 0
        for j in range(i, n - m + 1):
            if nums[j] > max_num:
                max_num = nums[j]
                max_idx = j
                if nums[j] == 9:
                    break
        answer += str(max_num)
        i = max_idx + 1
        m -= 1
    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))