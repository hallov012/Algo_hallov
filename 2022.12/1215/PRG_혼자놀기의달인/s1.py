def solution(cards):
    answer = 0
    n = len(cards)
    data = [0] + cards
    def firstPlay():
        for i in range(1, n+1):
            checked = [0] * (n+1)
            fisrt = [i]
            checked[i] = 1
            idx = data[i]
            while not checked[idx]:
                checked[idx] = 1
                fisrt.append(idx)
                idx = data[idx]
            secondPlay(checked, fisrt)

    def secondPlay(checked, first):
        nonlocal answer
        for i in range(1, n+1):
            if not checked[i]:
                second = [i]
                checked_data = checked[::]
                checked_data[i] = 1
                idx = data[i]
                while not checked_data[idx]:
                    checked_data[idx] = 1
                    idx = data[idx]
                    second.append(idx)
                answer = max(answer, len(first) * len(second))

    firstPlay()

    return answer

print(solution([8, 6, 3, 7, 2, 5, 1, 4]))