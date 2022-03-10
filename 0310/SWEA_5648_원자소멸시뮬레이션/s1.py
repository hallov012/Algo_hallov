import sys
sys.stdin = open('input.txt')

T = int(input())

atoms = [[0] * 4001 for _ in range(4001)]

for tc in range(1, T+1):
    n = int(input())
    position = []
    direction = []
    power = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    ans = 0
    is_it_boom = [1] * n
    for i in range(n):
        y, x, d, p = map(int, input().split())
        position.append([2*(x+1000), 2*(y+1000)])
        direction.append(d)
        power.append(p)
    for i in range(n):
        x, y = position[i]
        atoms[x][y] = 1
    while 1:
        boom_position = []
        for i in range(n):
            if is_it_boom[i]:  # 아직 남아있으면 이동해줘야 함
                a = direction[i]
                atoms[position[i][0]][position[i][1]] -= 1
                position[i][0] += dx[a]
                position[i][1] += dy[a]
                if 0 <= position[i][0] < 4001 and 0 <= position[i][1] < 4001:
                    if atoms[position[i][0]][position[i][1]] != 0:
                        if [position[i][0], position[i][1]] not in boom_position:
                            boom_position.append([position[i][0], position[i][1]])
                    atoms[position[i][0]][position[i][1]] += 1
                else:
                    is_it_boom[i] = 0
        if boom_position:
            for booms in boom_position:
                atoms_lst = []
                for i in range(n):
                    if position[i] == booms:
                        atoms_lst.append(i)
                if len(atoms_lst) > 1:
                    for j in atoms_lst:
                        ans += power[j]
                        is_it_boom[j] = 0
                    atoms[booms[0]][booms[1]] = 0
        if sum(is_it_boom) == 0:
            break
    print(f'#{tc} {ans}')

