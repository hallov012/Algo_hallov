from collections import deque 

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    # 제일 위의 카드 바닥에 버리기
    cards.popleft()
    # 제일 위의 카드를 뒤로 옮기기
    cards.append(cards[0])
    cards.popleft()

print(cards[0])
