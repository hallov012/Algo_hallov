from itertools import permutations

def solution(users, emoticons):
    ans = []
    users.sort()
    percent = []
    cost_dic = {}
    for num in [10, 20, 30, 40]:
        if num >= users[0][0]:
            percent.append(num)
            lst = []
            for cost in emoticons:
                lst.append(int(cost * (100 - num) / 100))
            cost_dic[num] = lst
    percent = percent * (len(emoticons))
    cases = list(set(permutations(percent, len(emoticons))))
    cases.sort()
    print(cases)
    for case in cases:
        temp = [0, 0]
        for j in range(len(users)):
            user = users[j]
            cost = 0
            for i in range(len(emoticons)):
                if user[0] <= case[i]:
                    cost += cost_dic[case[i]][i]
                    if cost >= user[1]:
                        temp[0] += 1
                        break
            if cost < user[1]:
                temp[1] += cost
        ans.append(temp)

    ans.sort(reverse=True)
    return ans[0]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))