def solution(sequence, k):
    ans = []
    n = len(sequence)
    r = 0
    cnt = 0
    for l in range(n):
        while r < n and cnt < k:
            cnt += sequence[r]
            r += 1

        if cnt == k:
            if not ans:
                ans = [l, r-1]
            else:
                if ans[1] - ans[0] > (r-1) - l:
                    ans = [l, r-1]
        cnt -= sequence[l]
    return ans

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))