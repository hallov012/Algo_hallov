def solution(coin, cards):
    def check():


    def find(c, turn):
        nonlocal answer
        if c == 0 or turn == t:
            answer = max(answer, turn)
            return
        a, b = cards[m + 2*t], cards[m + 2*t + 1]
        # a만 가지는 경우
        cnt[a] += 1


    answer = 0
    n = len(cards)
    m = n // 3
    t = (n-m) // 2

    cnt = [0] * (n+1)
    for i in range(m):
        cnt[cards[i]] += 1

    return answer


data = [
    [4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]],
    [3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]],
    [2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]],
    [10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]
]

for coin, cards in data:
    print(solution(coin, cards))