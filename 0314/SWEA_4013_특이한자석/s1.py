import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    k = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]
    spins = [list(map(int, input().split())) for _ in range(k)]
    # idx 2랑 idx 6이 서로 마주본다
    for spin in spins:
        num, d = spin[0]-1, spin[1]
        if num == 0:
            changes = []
            for i in range(1, 4):
                if magnet[i-1][2] != magnet[i][6]:
                    changes.append(i)
                else:
                    break
        elif num == 3:
            changes = []
            for j in range(num-1, -1, -1):
                if magnet[j+1][6] != magnet[j][2]:
                    changes.append(j)
                else:
                    break
        else:
            changes = []
            for i in range(num+1, 4):
                if magnet[i-1][2] != magnet[i][6]:
                    changes.append(i)
                else:
                    break
            for j in range(num-1, -1, -1):
                if magnet[j+1][6] != magnet[j][2]:
                    changes.append(j)
                else:
                    break
        if d == 1:
            a = magnet[num].pop()
            magnet[num] = [a] + magnet[num]
            for change in changes:
                if (num - change) % 2:
                    a = magnet[change].pop(0)
                    magnet[change].append(a)
                else:
                    a = magnet[change].pop()
                    magnet[change] = [a] + magnet[change]
        else:
            a = magnet[num].pop(0)
            magnet[num].append(a)
            for change in changes:
                if (num - change) % 2:
                    a = magnet[change].pop()
                    magnet[change] = [a] + magnet[change]
                else:
                    a = magnet[change].pop(0)
                    magnet[change].append(a)
    ans = 0
    for i in range(4):
        if magnet[i][0]:
            ans += 2 ** i
    print(f'#{tc} {ans}')
