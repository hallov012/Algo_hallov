def solution(priorities, location):
    n = len(priorities)
    idx_lst = list(range(n))
    result = []
    while priorities:
        max_imp = max(priorities)
        importance = priorities.pop(0)
        idx = idx_lst.pop(0)
        if importance == max_imp:
            result.append(idx)
        else:
            priorities.append(importance)
            idx_lst.append(idx)
    answer = result.index(location) + 1
    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))