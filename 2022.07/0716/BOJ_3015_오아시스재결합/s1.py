import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
# stack 안에 (키, 같은 키를 가진 사람의 수)를 저장
# stack은 내림차순으로 정렬되게 된다
stack = []
ans = 0
for h in data:
    # 현재 사람보다 키가 작은 사람들은 stack에서 pop하여 그 수를 ans에 더해줌
    while stack and stack[-1][0] < h:
        ans += stack.pop()[1]
    # 현재 사람이 지금까지 나온 사람 중 가장 크다면 stack에 저장
    if not stack:
        stack.append((h, 1))
        continue
    # 현재 사람의 키와 stack top의 키가 같다면, stack에서 pop한 후 같은 키인 사람들의 수를 ans에 더해줌
    if stack[-1][0] == h:
        cnt = stack.pop()[1]
        ans += cnt
        # 현재 사람의 키보다 큰 사람이 있으면, 그 큰 사람은 현재 사람도 볼 수 있음(현재와 같은 키가 입력되어도 동일)
        if stack:
            ans += 1
        stack.append((h, cnt+1))
    # stack이 비어있지 않고, stack top이 더 큰 경우, 오른쪽은 볼 수 없고 왼쪽만 볼 수 있음
    else:
        stack.append((h, 1))
        ans += 1
print(ans)
