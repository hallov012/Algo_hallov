def solution(n, build_frame):
    answer = []
    pillar = [[0] * (n+1) for _ in range(n+1)]
    beam = [[0] * (n+1) for _ in range(n+1)]

    # 기둥 설치 조건
    # 1. 바닥 위
    # 2. 보의 한쪽 끝 부분 위
    # 3. 기둥의 위
    def can_pillar(x, y):
        if x == 0:
            return True
        else:
            if (y > 0 and beam[x][y-1]) or beam[x][y]:
                return True
            if pillar[x-1][y]:
                return True
        return False

    # 기둥 하나를 삭제할 때 확인 하는 것
    # 1. 위에 또 다른 기둥이 있는가? => 그러면 그 기둥은 다른 보와 연결되어 있는가
    # 2. 해당 기둥 위에 이어진 보가 있는가? => 그렇다면 그 보는 다른 기둥과 연결되어 있는가 / 보끼리 연결되어 있는가?
    def can_remove_pillar(x, y):
        if x < n and pillar[x+1][y]:
            if (y > 0 and beam[x+1][y-1]) or beam[x+1][y]:
                pass
            else:
                return False
        if x < n and y > 0 and beam[x+1][y-1]:
            flag = False
            if pillar[x][y-1]:
                flag = True
            if 1 < y and beam[x+1][y-2] and beam[x+1][y]:
                flag = True
            if not flag:
                return False
        if x < n and beam[x+1][y]:
            flag = False
            if y < n and pillar[x][y+1]:
                flag = True
            if 1 < y < n and beam[x+1][y-1] and beam[x+1][y+1]:
                flag = True
            if not flag:
                return False
        return True

    # 보 설치 조건
    # 1. 한쪽 끝 부분이 기둥 위
    # 2. 양 끝이 다른 보와 연결
    def can_beam(x, y):
        if pillar[x-1][y] or (y < n and pillar[x-1][y+1]):
            return True
        if 0 < y < n and beam[x][y-1] and beam[x][y+1]:
            return True
        return False

    # 보를 삭제할 때 확인하는 것
    # 1. 보 위에 기둥이 있는가? => 그 옆에 보가 기둥을 지탱할 수 있는가? / 그 및에 기둥이 또 있는가?
    # 2. 양 끝에 다른 보가 있는가? => 그 보들이 다른 기둥과 연결되어 있는가?
    def can_remove_beam(x, y):
        if pillar[x][y]:
            if beam[x][y-1] or pillar[x-1][y]:
                pass
            else:
                return False
        if y < n-1 and pillar[x][y+1]:
            if beam[x][y+1] or pillar[x-1][y]:
                pass
            else:
                return False
        if 0 < y < n-1 and beam[x][y-1] and beam[x][y+1]:
            if (pillar[x-1][y-1] or pillar[x-1][y]) and (pillar[x-1][y+1] or pillar[x-1][y+2]):
                pass
            else:
                return False
        return True


    for y, x, a, b in build_frame:
        # 기둥
        if not a:
            if b:
                if can_pillar(x, y):
                    pillar[x][y] = 1
            else:
                if can_remove_pillar(x, y):
                    pillar[x][y] = 0
        # 보
        else:
            if b:
                if can_beam(x, y):
                    beam[x][y] = 1
            else:
                if can_remove_beam(x, y):
                    beam[x][y] = 0

    for j in range(n+1):
        for i in range(n+1):
            if pillar[i][j]:
                answer.append([j, i, 0])
            if beam[i][j]:
                answer.append([j, i, 1])

    return answer


# print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
# print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))