from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    cnt = defaultdict(int)
    for num in tangerine:
        cnt[num] += 1
    sort_cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
    box = 0
    for key, value in sort_cnt:
        box += value
        answer += 1
        if box >= k:
            break
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))