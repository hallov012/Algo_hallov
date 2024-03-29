from collections import defaultdict, deque

"""
그래프의 수가 2일 때를 고려 못했음
"""

def solution(edges):
    answer = [0, 0, 0, 0]
    cnt = defaultdict(int)
    g = defaultdict(list)
    for a, b in edges:
        cnt[a] += 1
        g[a].append(b)

    cnt_lst = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
    node = cnt_lst[0][0]
    answer[0] = node

    m = 1000000
    visited = [0] * (m+1)
    for x in g[node]:
        visited[x] = 1
        cnt = 1
        edges = 0
        que = deque([x])
        dup = False
        while que:
            a = que.popleft()
            for b in g[a]:
                if b != node:
                    edges += 1
                    if not visited[b]:
                        visited[b] = 1
                        que.append(b)
                        cnt += 1
                    else:
                        dup = True
        if not dup:
            answer[2] += 1
        else:
            if cnt == edges:
                answer[1] += 1
            elif cnt + 1 == edges:
                answer[3] += 1

    return answer

data = [
    [[2, 3], [4, 3], [1, 1], [2, 1]],
    [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
]

for d in data:
    print(solution(d))