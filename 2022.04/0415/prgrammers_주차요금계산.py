from collections import defaultdict

def solution(fees, records):
    n = len(records)
    my_dic = defaultdict(list)
    for i in range(n):
        time, number, in_out = records[i].split()
        my_dic[number].append(time)
    my_dic = sorted(my_dic.items(), key=lambda item: item[0])
    m = len(my_dic)
    answer = [0] * m
    for i in range(m):
        data = my_dic[i]
        time = 0
        if len(data[1]) % 2:
            data[1].append('23:59')
        j = 0
        while j < len(data[1]):
            in_time = list(map(int, data[1][j].split(':')))
            out_time = list(map(int, data[1][j+1].split(':')))
            if out_time[1] - in_time[1] >= 0:
                time += out_time[1] - in_time[1]
            else:
                time += out_time[1] - in_time[1] + 60
                out_time[0] -= 1
            time += (out_time[0] - in_time[0]) * 60
            j += 2
        payment = 0
        if time <= fees[0]:
            payment = fees[1]
        else:
            payment = fees[1]
            if (time-fees[0])%fees[2] == 0:
                payment += fees[3] * ((time-fees[0])//fees[2])
            else:
                payment += fees[3] * ((time-fees[0])//fees[2] + 1)
        answer[i] = payment
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))