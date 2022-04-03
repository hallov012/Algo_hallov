def solution(n, lost, reserve):
    def dfs(cnt, idx):
        nonlocal answer
        if cnt + (n - idx) <= answer:
            return
        if idx == n + 1:
            answer = max(answer, cnt)
            return
        if idx not in lost:
            dfs(cnt + 1, idx + 1)
        else:
            if cnt_cloth[idx - 1] > 0:
                cnt_cloth[idx - 1] -= 1
                dfs(cnt + 1, idx + 1)
                cnt_cloth[idx - 1] += 1
            if cnt_cloth[idx + 1] > 0:
                cnt_cloth[idx + 1] -= 1
                dfs(cnt + 1, idx + 1)
                cnt_cloth[idx + 1] += 1
            dfs(cnt, idx + 1)
    answer = 0
    cnt_cloth = [0] * (n + 2)
    for num in reserve:
        if num in lost:
            lost.remove(num)
        else:
            cnt_cloth[num] += 1
    dfs(0, 1)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))

