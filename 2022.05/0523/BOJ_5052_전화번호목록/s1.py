import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    ans = 'YES'
    n = int(input())
    numbers = [str(input().strip()) for _ in range(n)]
    numbers.sort()
    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            ans = 'NO'
            break
    print(ans)

