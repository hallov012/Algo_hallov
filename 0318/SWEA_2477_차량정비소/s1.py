import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    a_time = list(map(int, input().split()))
    b_time = list(map(int, input().split()))
    arrive_time = list(map(int, input().split()))
    a_list, a_list_idx = [0] * N, [0] * N
    b_list, b_list_idx = [0] * M, [0] * M
    a_user = [[] for _ in range(N)]
    b_user = [[] for _ in range(M)]
    waiting_user = []
    end = 0
    while end < K:
        # 정비 창구 처리
        for k in range(M):
            if b_list[k] > 0:
                b_list[k] -= 1
                if not b_list[k]:
                    end += 1
                    b_list_idx[k] = 0


        # 기다리고 있는 고객 처리
        cnt = 0
        for user in waiting_user:
            for b in range(M):
                if not b_list[b] and not b_list_idx[b]:
                    b_list[b] = b_time[b]
                    b_list_idx[b] = user[1]
                    b_user[b].append(user[1])
                    cnt += 1
                    break
        for _ in range(cnt):
            waiting_user.pop(0)

        # 접수 창고 내에서의 처리
        for j in range(N):
            if a_list[j] > 0:
                a_list[j] -= 1
                if not a_list[j]:
                    if 0 in b_list:
                        for v in range(M):
                            if not b_list[v]:
                                b_list[v] = b_time[v]
                                b_list_idx[v] = a_list_idx[j]
                                b_user[v].append(a_list_idx[j])
                                a_list_idx[j] = 0
                                break
                    else:
                        waiting_user.append([j, a_list_idx[j]])
                        a_list_idx[j] = 0

        # 도착한 시간 순으로 접수 창고에 넣는 처리
        for i in range(K):
            if not arrive_time[i]:
                for a in range(N):
                    if not a_list[a] and not a_list_idx[a]:
                        a_list[a] = a_time[a]
                        a_list_idx[a] = i+1
                        a_user[a].append(i+1)
                        arrive_time[i] = -1
                        break
            elif arrive_time[i] > 0:
                arrive_time[i] -= 1

    ans_a = a_user[A - 1]
    ans_b = b_user[B - 1]
    intersection = list(set(ans_a) & set(ans_b))
    ans = 0
    if not intersection:
        ans = -1
    else:
        for v in intersection:
            ans += v
    print(f'#{tc} {ans}')