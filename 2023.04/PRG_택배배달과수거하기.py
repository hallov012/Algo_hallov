def solution(cap, n, deliveries, pickups):
    ans = 0
    deliveries.reverse()
    pickups.reverse()
    d_cnt, p_cnt = 0, 0
    for i in range(n):
        d_cnt += deliveries[i]
        p_cnt += pickups[i]
        while d_cnt > 0 or p_cnt > 0:
            d_cnt -= cap
            p_cnt -= cap
            ans += (n-i) * 2
    return ans

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))