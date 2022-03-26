import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    check = False
    for spicy in scoville:
        heapq.heappush(heap, spicy)
    for _ in range(len(heap)):             # 스코빌의 수 만큼 시행
        a = heapq.heappop(heap)
        if a >= K:                         # 가장 작은 수가 K 이상이라면 조건 충족
            check = True
            break
        if not heap:                       # 마지막까지 가장 작은 수가 조건을 만족하지 못한 경우 => 더이상 pop 할게 없음
            break
        b = heapq.heappop(heap)
        c = a + 2 * b
        heapq.heappush(heap, c)
        answer += 1
    if check:
        return answer
    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 7))