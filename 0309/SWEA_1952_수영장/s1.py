import sys
sys.stdin = open('input.txt')

def somebody_help_me(s, cost_check):
    global cost
    if s >= 12:
        if cost > cost_check:
            cost = cost_check
        return
    if cost_lst[s] > 0:
        month_plan = []
        for i in range(3):
            if s+i < 12:
                month_plan.append(cost_lst[s+i])
        if sum(month_plan) > price[2]:
            somebody_help_me(s+3, cost_check+price[2])
        somebody_help_me(s+1, cost_check+cost_lst[s])
    else:
        somebody_help_me(s+1, cost_check)

T = int(input())

for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    cost_lst = [0] * 12
    for i in range(12):
        if plan[i] > 0:
            day_cost = price[0] * plan[i]
            if day_cost < price[1]:
                cost_lst[i] = day_cost
            else:
                cost_lst[i] = price[1]
    cost = price[3]
    somebody_help_me(0, 0)
    print(f'#{tc} {cost}')