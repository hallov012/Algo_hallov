from collections import defaultdict, deque

def solution(n, paths, gates, summits):
    answer = [0, 10 ** 7]
    g = defaultdict(list)
    gate_c = [0] * (n+1)
    summit_c = [0] * (n+1)
    for i in range(len(paths)):
        s, e, d = paths[i]
        g[s].append((e, d))
        g[e].append((s, d))
    for gate in gates:
        gate_c[gate] = 1
    for summit in summits:
        summit_c[summit] = 1

    # def find(s, check):
    #     nonlocal answer
    #     if summit_c[s]:
    #         if answer[1] > check:
    #             answer = [s, check]
    #         elif answer[1] == check:
    #             answer[0] = min(answer[0], s)
    #         return
    #     if check > answer[1]:
    #         return
    #     for e, d in g[s]:
    #         if not visited[e] and not gate_c[e]:
    #             visited[e] = 1
    #             find(e, max(check, d))
    #             visited[e] = 0

    def find(x):
        nonlocal answer
        que = deque([(x, 0)])
        while que:
            s, value = que.popleft()
            if summit_c[s]:
                if value < answer[1]:
                    answer = [s, value]
                elif value == answer[1]:
                    answer[0] = min(answer[0], s)
            for e, d in g[s]:
                if not gate_c[e]:
                        value = max(value, d)
                        if value < visited[e]:
                            visited[e] = value
                            que.append((e, value))

    inf = 987654321
    for gate in gates:
        visited = [inf] * (n+1)
        visited[gate] = 0
        find(gate)

    #
    # for gate in gates:
    #     visited = [0] * (n+1)
    #     visited[gate] = 1
    #     find(gate, 0)

    return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))