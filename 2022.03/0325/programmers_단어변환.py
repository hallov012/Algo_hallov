from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    if target not in words:
        return answer
    def compare(start, end):
        diff = 0
        for i in range(len(start)):
            if start[i] != end[i]:
                diff += 1
        if diff == 1:
            return True
        return False
    que = deque([[begin, 0]])
    while que:
        now, cnt = que.popleft()
        if now == target:
            answer = cnt
            break
        for i in range(len(words)):
            if compare(now, words[i]) and not visited[i]:
                visited[i] = 1
                que.append([words[i], cnt + 1])
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))