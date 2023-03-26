def solution(today, terms, privacies):
    answer = []
    term_data = {}
    ty, tm, td = map(int, today.split('.'))
    today_data = 12 * 28 * ty + 28 * tm + td
    for term in terms:
        type, m = term.split()
        term_data[type] = int(m)

    for i in range(len(privacies)):
        item = privacies[i]
        date, type = item.split()
        y, m, d = map(int, date.split('.'))
        date_data = 12 * 28 * y + 28 * m + d
        date_data += term_data[type] * 28 - 1
        if date_data < today_data:
            answer.append(i+1)
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
