from collections import deque

def solution(coin, cards):
    """
    코인을 안쓰고 가져올 수 있다면 안쓰고 해결
    안된다면 1개 => 2개 사용
    최대한 코인을 적게 쓰면서 한 턴을 마치기
    """

    def check(a_lst, b_lst):
        for a in a_lst:
            if t - a in b_lst:
                a_lst.remove(a)
                b_lst.remove(t - a)
                return True
        return False

    n = len(cards)
    m = n // 3
    t = n + 1
    have, left, pend = cards[:m], deque(cards[m:]), []
    round = 1

    while left and coin >= 0:
        x, y = left.popleft(), left.popleft()
        pend.append(x)
        pend.append(y)
        # 가지고 있는 것 중에 결정
        if check(have, have):
            pass
        # 가진 것, 팬딩 된 것 중에 결정
        elif coin > 0 and check(have, pend):
            coin -= 1
        # 팬딩 된 것 중에 결정
        elif coin > 1 and check(pend, pend):
            coin -= 2
        else:
            break
        round += 1
    return round