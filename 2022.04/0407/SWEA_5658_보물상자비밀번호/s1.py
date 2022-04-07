import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

# 16진수 -> 10진수 변환 방법 int('0x__', 16)
for tc in range(1, T+1):
    n, k = map(int, input().split())
    words = deque(list(map(str, input())))
    nums = []
    m = n // 4
    for _ in range(m):
        char = words.popleft()
        words.append(char)
        for i in range(4):
            sub = ''
            for j in range(m):
                sub += words[i*m+j]
            num = int('0x'+sub, 16)
            if num not in nums:
                nums.append(num)
    nums.sort(reverse=True)
    print(f'#{tc} {nums[k-1]}')
