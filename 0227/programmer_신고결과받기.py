def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_cnt = [0] * len(id_list)
    report_set = list(set(report))
    reporter_lst = [[] for _ in range(len(id_list))]
    for i in range(len(report_set)):
        reporter, warning_user = map(str, report_set[i].split())
        reporter_lst[id_list.index(warning_user)].append(reporter)
    for i in range(len(id_list)):
        if len(reporter_lst[i]) >= k:
            for j in reporter_lst[i]:
                answer[id_list.index(j)] += 1
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))