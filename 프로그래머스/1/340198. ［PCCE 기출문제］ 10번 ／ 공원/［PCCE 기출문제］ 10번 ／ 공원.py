def solution(mats, park):
    h, w = len(park), len(park[0])
    mats.sort(reverse=True)  # 큰 것부터 시도하면 조기 종료 가능

    for mat in mats:
        for i in range(h - mat + 1):
            for j in range(w - mat + 1):
                can_place = True
                for x in range(i, i + mat):
                    for y in range(j, j + mat):
                        if park[x][y] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    return mat  # 가장 큰 것부터 찾았으므로 바로 리턴

    return -1