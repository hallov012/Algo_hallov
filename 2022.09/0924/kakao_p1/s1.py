def solution(today, terms, privacies):
    ans = []
    today_year, today_month, today_date = map(int, today.split("."))

    term_dic = {}
    for term in terms:
        term_lst = term.split(" ")
        term_dic[term_lst[0]] = int(term_lst[1])

    for i in range(len(privacies)):
        date, term_type = privacies[i].split(" ")
        year, month, date = map(int, date.split("."))
        month += term_dic[term_type]
        if month > 12:
            add_y = month // 12
            month %= 12
            if not month:
                month = 12
                add_y -= 1
            year += add_y

        if today_year > year:
            ans.append(i+1)
            continue
        elif today_year < year:
            continue
        else:
            if today_month > month:
                ans.append(i+1)
                continue
            elif today_month < month:
                continue
            else:
                if today_date >= date:
                    ans.append(i+1)

    return ans

print(solution(
"2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))

print(solution(
"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

