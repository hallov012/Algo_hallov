import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    V, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[] for _ in range(V+1)]
    get_in = [0] * (V+1)
    for i in range(E):
        G[temp[2*i]].append(temp[2*i+1])
        get_in[temp[2*i+1]] += 1
    start = []
    for i in range(1, V+1):
        if not get_in[i]:
            start.append(i)
    ans = []
    while start:
        now = start.pop()
        ans.append(now)
        for can_go in G[now]:
            get_in[can_go] -= 1
            if not get_in[can_go]:
                start.append(can_go)
    print(f'#{tc}', *ans)



