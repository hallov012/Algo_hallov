import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, 10 + 1):
    tc = int(input())
    queue = list(map(int, input().split()))
    # print(queue[7])

    while True:
        flag = True
        for i in range(1, 6):
            queue[0] -= i
            queue.append(queue.pop(0))
            if queue[-1] <= 0:
                queue[-1] = 0
                flag = False
                break
        if not flag:
            break

    print(f'#{t}', *queue)