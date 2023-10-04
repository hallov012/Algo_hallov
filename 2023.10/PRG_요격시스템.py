def solution(targets):
    ans = 0
    targets.sort(key=lambda x: [x[1], x[0]])
    end = 0
    for x, y in targets:
        if x >= end:
            ans += 1
            end = y
    return ans

print(solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]))