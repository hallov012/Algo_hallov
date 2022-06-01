import sys
sys.stdin = open('input.txt')

def check(sum):
    global ans
    if len(stack) == n:
        pass
    else:
        for i in range(n):
            # stack이 비어있으면 바로 추가
            if not stack:
                stack.append(i)
                sum += nums[i]
                if sum == s:
                    ans += 1
                check(sum)
                stack.pop()
                sum -= nums[i]
            # 무언가 들어있다면 들어있지 않은 애들만 추가
            elif stack[-1] < i:
                stack.append(i)
                sum += nums[i]
                if sum == s:
                    ans += 1
                check(sum)
                stack.pop()
                sum -= nums[i]

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
stack = []
ans = 0
check(0)
print(ans)

