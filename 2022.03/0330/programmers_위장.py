from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for name, types in clothes:
        dic[types] += 1
    for case in dic.values():
        answer *= case + 1
    answer -= 1
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))