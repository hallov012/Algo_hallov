import sys, heapq
from collections import defaultdict
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, b = map(int, input().split())
    t_dic = defaultdict(list)
    for _ in range(n):
        t, n, p, q = input().split()
        # 가격이 낮고, 가격이 같을 경우 품질이 좋은거
        heapq.heappush(t_dic[t], (int(p), -int(q)))

    cost = 0
    parts = []
    t_n = len(t_dic.keys())
    for t in t_dic.keys():
        p, q = heapq.heappop(t_dic[t])
        cost += p
        # 품질이 낮고 같을 경우 가격이 비싼 것
        heapq.heappush(parts, (-q, -p, t))

    while True:
        # 제일 품질이 낮은 제품을 가져옴
        q, p, t = heapq.heappop(parts)
        p *= -1

        # 품질이 더 좋은 다른 제품을 탐색
        while t_dic[t]:
            n_p, n_q = heapq.heappop(t_dic[t])
            n_q *= -1
            if n_q > q:
                cost += n_p - p
                # 예산 안에 들어가면 새로운 부품으로 교체
                if cost <= b:
                    heapq.heappush(parts, (n_q, -n_p, t))
                break
        # 새로운 제품을 추가하지 못했다 => 더이상 변경 할 수 없음
        if len(parts) != t_n:
            print(q)
            break




