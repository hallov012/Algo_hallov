from collections import defaultdict, deque

def solution(edges):
    answer = [0, 0, 0, 0]
    out_g = defaultdict(int)
    in_g = defaultdict(int)
    g = defaultdict(list)
    nodes = set()
    for a, b in edges:
        out_g[a] += 1
        in_g[b] += 1
        nodes.add(a)
        nodes.add(b)
        g[a].append(b)

    for x in nodes:
        # 나가는 것만 있으면 정점
        if not in_g[x] and out_g[x] >= 2:
            answer[0] = x
            node = x

    m = 1000000
    visited = [0] * (m + 1)
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