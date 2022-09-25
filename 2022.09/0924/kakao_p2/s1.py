def solution(cap, n, deliveries, pickups):
    ans = 0
    plan = n-1
    d_cnt = sum(deliveries)
    p_cnt = sum(pickups)
    while True:
        if not d_cnt and not p_cnt:
            break
        while not deliveries[plan] and not pickups[plan]:
            plan -= 1
        go = cap
        back = 0
        last_go, last_back = 0, 0
        for i in range(plan, -1, -1):
            if go and d_cnt:
                if deliveries[i]:
                    if go >= deliveries[i]:
                        go -= deliveries[i]
                        d_cnt -= deliveries[i]
                        deliveries[i] = 0
                        last_go = i-1
                    else:
                        deliveries[i] -= go
                        d_cnt -= go
                        go = 0
                        last_go = i
            if back < cap and p_cnt:
                if pickups[i]:
                    if back + pickups[i] <= cap:
                        back += pickups[i]
                        p_cnt -= pickups[i]
                        pickups[i] = 0
                        last_back = i-1
                    else:
                        pickups[i] -= cap - back
                        p_cnt -= cap - back
                        back = cap
                        last_back = i
            if not go and back == cap:
                break
        ans += 2 * (plan+1)
        plan = max(last_go, last_back)

    return ans

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))