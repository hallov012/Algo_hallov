from itertools import permutations

def solution(users, emoticons):
    ans = [0, 0]
    percent = [10, 20, 30, 40] * len(emoticons)
    cases = set(list(permutations(percent, len(emoticons))))
    for case in cases:
        temp = [0, 0]
        for j in range(len(users)):
            if temp[0] + len(users) - j < ans[0]:
                break
            user = users[j]
            cost = 0
            for i in range(len(emoticons)):
                if user[0] <= case[i]:
                    cost += emoticons[i] * (100 - case[i]) / 100
            if cost >= user[1]:
                temp[0] += 1
            else:
                temp[1] += cost
        if temp[0] > ans[0]:
            ans = temp
        elif temp[0] == ans[0]:
            if temp[1] > ans[1]:
                ans = temp
    return ans

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))