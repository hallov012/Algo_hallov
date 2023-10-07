def solution(picks, minerals):
    ans = 0
    n = len(minerals)
    if n > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]
        n = sum(picks) * 5

    cnt = [[0] * 3 for _ in range(10)]
    for i in range(n):
        if minerals[i] == 'diamond':
            cnt[i//5][0] += 1
        elif minerals[i] == 'iron':
            cnt[i//5][1] += 1
        else:
            cnt[i//5][2] += 1

    cnt.sort(reverse=True)

    for d, i, s in cnt:
        if picks[0] > 0:
            picks[0] -= 1
            ans += sum([d, i, s])
        elif picks[1] > 0:
            picks[1] -= 1
            ans += 5 * d + i + s
        else:
            picks[2] -= 1
            ans += 25 * d + 5 * i + s

    return ans

print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))